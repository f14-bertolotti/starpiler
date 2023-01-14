from lark.visitors import v_args, Visitor, Transformer
from lark.tree import Tree
from lark import Token

from src.semantics.types import *
from src.utils import SmallMeta
from src.utils import TreeAnon
from src.utils import SmallMeta

LinkedNodeType = SType("LinkedNode", {})
LinkedNodeType["next"] = Pointer(LinkedNodeType)
LinkedNodeType["element"] = Pointer(Int8())
LinkedNodeType["bsize"] = Int64()
LinkedNodeType["marked"] = Int64()
LinkedNodeType["start"] = Pointer(FType([Pointer(LinkedNodeType), Pointer(Int8()), Int64()], Pointer(LinkedNodeType)))
LinkedNodeType["isLast"] = Pointer(FType([Pointer(LinkedNodeType)], Int64()))
LinkedNodeType["getLast"] = Pointer(FType([Pointer(LinkedNodeType)],Pointer(LinkedNodeType)))
LinkedNodeType["size"] = Pointer(FType([Pointer(LinkedNodeType)],Int64()))
LinkedNodeType["append"] = Pointer(FType([Pointer(LinkedNodeType),Pointer(LinkedNodeType)],Pointer(LinkedNodeType))) 
LinkedNodeType["print"] = Pointer(FType([Pointer(LinkedNodeType)],Pointer(LinkedNodeType)))
LinkedNodeType["printAll"] = Pointer(FType([Pointer(LinkedNodeType)],Pointer(LinkedNodeType)))
LinkedNodeType["fromElementPointer"] = Pointer(FType([Pointer(LinkedNodeType),Pointer(Int8())],Pointer(LinkedNodeType)))
LinkedNodeType["end"] = Pointer(FType([Pointer(LinkedNodeType)], Void()))

GCType = SType("GC", {})
GCType["node"] = Pointer(LinkedNodeType)
GCType["roots"] = Pointer(LinkedNodeType)
GCType["start"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["push"] = Pointer(FType([Pointer(GCType), Pointer(Int8()), Int64()], Pointer(GCType)))
GCType["pop"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["mark_root"] = Pointer(FType([Pointer(GCType), Pointer(Int8())], Pointer(GCType)))
GCType["mark"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["unmark"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["sweep"] = Pointer(FType([Pointer(GCType)], Pointer(GCType)))
GCType["end"] = Pointer(FType([Pointer(GCType)], Void()))

gcImportTree = Tree(Token("RULE", "spplang_import"), [
                Token("FROM", "from"), 
                Tree(Token("RULE", "spplang_string"), [Token("__ANON__", "\"src/testing/spplang/programs/gc/GC.spp\"")]), 
                Token("IMPORT", "import"), 
                Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "GC")]), 
                Token("AS", "as"), 
                Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "GC")]), 
                Token("SEMICOLON", ";")], SmallMeta(type=GCType))
gcRefImportTree = Tree(Token("RULE", "spplang_import"), [
                Token("FROM", "from"), 
                Tree(Token("RULE", "spplang_string"), [Token("__ANON__", "\"src/testing/spplang/programs/gc/GC.spp\"")]), 
                Token("IMPORT", "import"), 
                Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "gc")]), 
                Token("AS", "as"), 
                Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "gc")]), 
                Token("SEMICOLON", ";")], SmallMeta(type=GCType))

gcMainDefinition = Tree(Token('RULE', 'spplang_stmt_expr'), [
    Tree(Token('RULE', 'spplang_assignement'), [
        Tree(Token('RULE', 'spplang_reference'), [
            Token('AMPERSAND', '&'), 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')])]), 
        Token('EQUAL', '='), 
        Tree(Token('RULE', 'spplang_new'), [
            Token('NEW', 'new'), 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'GC')]), 
            Token('LPAR', '('), 
            Token('RPAR', ')')])]), 
    Token('SEMICOLON', ';')])

gcMainEnd = Tree(Token('RULE', 'spplang_stmt_expr'), [
    Tree(Token('RULE', 'spplang_function_call'), [
        Tree(Token('RULE', 'spplang_struct_access'), [
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
            Token('DOT', '.'), 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'end')])]), 
        Token('LPAR', '('), 
        Token('RPAR', ')')]), 
    Token('SEMICOLON', ';')])

gcMainType = Tree(Token('RULE', 'ssharplang_ftype'), [
    Tree(Token('RULE', 'ssharplang_ptype'), [
        Token('LPAR', '(')]), 
    Tree(Token('RULE', 'ssharplang_rtype'), [
        Token('__ANON__', '->'), 
        Tree(Token('RULE', 'ssharplang_int64'), [
            Token('INT64', 'int64')]), 
        Token('RPAR', ')')])])

gcPop = Tree(Token('RULE', 'spplang_stmt_expr'), [
    Tree(Token('RULE', 'spplang_function_call'), [
        Tree(Token('RULE', 'spplang_struct_access'), [
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
            Token('DOT', '.'), 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'pop')])]), 
        Token('LPAR', '('), 
        Token('RPAR', ')')]), 
    Token('SEMICOLON', ';')])


class SSharpOnly(Visitor):
    def __default__(self, tree):
        if not tree.data.startswith("ssharplang"): raise ValueError(f"Only ssharplang nodes allowed. found {tree}")
        return super().__default__(tree)

class AddBeforeReturn(Transformer):

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree
        super().__init__(*args, **kwargs)

    def __default__(self, data, children, meta):
        return super().__default__(data, [sub for child in children for sub in (child if isinstance(child,list) else [child])], meta)

    @v_args(tree=True)
    def ssharplang_return(self, tree):
        return [self.tree, tree]



class GC(Transformer):

    mainMethodApplied = False
    def __init__(self, *args, **kwargs):
        self.applied = False
        self.mainMethod = None
        super().__init__(*args, **kwargs)

    @v_args(meta=True)
    def ssharplang_start(self, meta, nodes):

        if all([node != gcImportTree for node in nodes if node.data == "spplang_import"]):
            self.applied = True
            res = Tree(Token("RULE","ssharplang_start"), [gcImportTree, gcRefImportTree] + nodes + ([self.mainMethod] if not GC.mainMethodApplied else []), meta)
            GC.mainMethodApplied = True
            return res
        return Tree(Token("RULE","ssharplang_start"), nodes, meta)


    @v_args(meta=True)
    def ssharplang_tname(self, meta, nodes):
        basemeta = meta.clone()
        ptrmeta = meta.clone()
        basemeta.type = basemeta.type.base
        ptrmeta.type = Pointer(meta.type.base)
        return Tree(Token('RULE', 'spplang_pointer'), [
            Tree(Token('RULE', 'spplang_tname'), [
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[0].children[0])], basemeta)], basemeta), 
            Token('STAR', '*')], ptrmeta)


    @v_args(meta=True)
    def ssharplang_block(self, meta, nodes):
        pops = [gcPop for node in nodes if node.data in {"ssharplang_declaration_assignment", "ssharplang_auto_assignment"}]
        returnPos = [i for i,node in enumerate(nodes) if node.data in {"ssharplang_return_void", "ssharplang_return"}][0]
        for pop in pops: nodes.insert(returnPos, pop)
        return Tree(Token("RULE", "ssharplang_block"), nodes, meta)


    @v_args(meta=True)
    def ssharplang_new(self, meta, nodes):
        meta = SmallMeta(nodes[1].meta.start_line, nodes[1].meta.end_line, nodes[1].meta.start_column, nodes[1].meta.end_column, Pointer(meta.type))
        return Tree(Token('RULE', 'spplang_stmt_expr'), [
            Tree(Token('RULE', 'spplang_cast'), [
                Tree(Token('RULE', 'spplang_function_call'), [
                    Tree(Token('RULE', 'spplang_struct_access'), [
                        Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                        Token('DOT', '.'), 
                        Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'push')])]), 
                    Token('LPAR', '('), 
                    Tree(Token('RULE', 'spplang_expression_sequence'), [
                        Tree(Token('RULE', 'spplang_new'), [
                            Token('NEW', 'new'), 
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[1].children[0].value)], meta), 
                            Token('LPAR', '('), 
                            Token('RPAR', ')')])], meta), 
                    Token('RPAR', ')')]), 
                Token('AS', 'as'), 
                Tree(Token('RULE', 'spplang_pointer'), [
                    Tree(Token('RULE', 'spplang_tname'), [
                        Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[1].children[0].value)])]), 
                    Token('STAR', '*')])], meta), 
            Token('SEMICOLON', ';')])


    @v_args(meta=True)
    def ssharplang_method_definition(self, meta, nodes):

        if nodes[2].children[0] == "__main__" and \
           TreeAnon().transform(nodes[1]) == gcMainType: 
            self.applied= True
            self.mainMethod = \
                Tree(Token('RULE', 'spplang_function_definition'), [
                    Token('DEF', 'def'), 
                    Tree(Token('RULE', 'spplang_int64'), [Token('INT64', 'int64')]), 
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', 'start')]), 
                    Tree(Token('RULE', 'spplang_parameter_seq_def'), [
                        Token('LPAR', '('), 
                        Token('RPAR', ')')]), 
                    Token('DOES', 'does'), 
                    Tree(Token('RULE', 'spplang_block'), [gcMainDefinition, *nodes[5].children]),
                    Token('SEMICOLON', ';')])
            self.mainMethod = AddBeforeReturn(gcMainEnd).transform(self.mainMethod)
            return Tree(Token("RULE","delete"),[])
        return Tree(Token("RULE", "ssharplang_method_definition"), nodes, meta)
        

    @v_args(meta=True)
    def ssharplang_class_definition(self, meta, nodes):
        return Tree("ssharplang_class_definition", [node for node in nodes if not (isinstance(node,Tree) and node.data == "delete")], meta)




def gc(parseTree) -> Tree:
    SSharpOnly().visit(parseTree)
    return GC().transform(parseTree)
 

