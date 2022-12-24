
from lark.visitors import v_args, Transformer
from lark.tree     import Tree
from lark          import Token
from lark          import Lark

from src.syntax       import Language
from src.transpilers  import addBeforeReturn
from src.syntax.slang import stmtexpr, functionCall, functionDeclaration, globalAssignement
from src.utils        import NotAppliedException

import copy

functionCallLang        = Lark(Language(       functionCall).toLark(), keep_all_tokens = True)
globalAssignementLang   = Lark(Language(  globalAssignement).toLark(), keep_all_tokens = True)
funDeclarationLang      = Lark(Language(functionDeclaration).toLark(), keep_all_tokens = True)
statementExpressionLang = Lark(Language(stmtexpr).toLark(), keep_all_tokens            = True)

freeDeclaration = funDeclarationLang.parse("def void free(int8*);")
freeAssignement = globalAssignementLang.parse("def (int8* -> void)* __free = &free;")
freeStatement   = statementExpressionLang.parse("&__free(this as int8*);")

class Classes(Transformer):

    def __init__(self, *args, **kwargs):
        self.add_free   = False
        self.free_added = False
        super().__init__(*args, **kwargs)

    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if self.add_free and not self.free_added: raise NotAppliedException()
        return res


    @v_args(meta=True)
    def spplang_start(self, meta, nodes):
        free = []
        globalAssignements = [node for node in nodes if isinstance(node, Tree) and node.data == "slang_global_assignement"]
        if self.add_free and not any(ass.children[1].children[2].children[0].value == "__free" for ass in globalAssignements):
            free = [copy.deepcopy(freeDeclaration), copy.deepcopy(freeAssignement)] 
            self.free_added = True
        return Tree(Token("RULE","spplang_start"), free + [sub for child in nodes for sub in (child if isinstance(child, list) else [child])], meta)
    

    @v_args(meta = True)
    def spplang_class(self, meta, nodes):
        
        # check exactly one "end" method 
        endMethods = [node for node in nodes[3:-1] if isinstance(node,Tree) and node.data == "spplang_method_definition" and node.children[2].children[0] == "end" ] 
        if len(endMethods) != 1: raise ValueError("class has 0 or >1 \"end\" methods")

        # check exactly one "start" method
        startMethods = [node for node in nodes[3:-1] if isinstance(node,Tree) and node.data == "spplang_method_definition" and node.children[2].children[0] == "start"]
        if len(startMethods) != 1: raise ValueError("class has 0 or >1 \"start\" methods")
        
        # adds &free(this as int8*) before each return in the "end" method;
        endMethods[-1] = addBeforeReturn(copy.deepcopy(freeStatement), endMethods[-1])
        self.add_free = True


        # base struct
        baseStruct = Tree(Token("RULE", "slang_struct"), [
            Token("STRUCT", "struct"), 
            Tree(Token("RULE", "slang_tname"), [nodes[1]]), 
            Token("WITH", "with"), 
            Token("SEMICOLON", ";")], meta)

        additionalFunctions = list()
        for node in nodes[3:-1]:
            if isinstance(node, Tree) and node.data == "spplang_field_declaration":
                # add struct declaration
                baseStruct.children.insert(-1, 
                                           Tree(Token("RULE", "slang_struct_declaration"), [
                                               node.children[1], 
                                               node.children[2], 
                                               Token("SEMICOLON", ";")], meta=copy.deepcopy(node.meta))
                                           )
            elif isinstance(node, Tree) and node.data == "spplang_field_definition":
                # add struct definition
                baseStruct.children.insert(-1, 
                                           Tree(Token("RULE", "slang_struct_definition"), [
                                               node.children[1], 
                                               node.children[2], 
                                               Token("EQUAL", "="), 
                                               node.children[4], 
                                               Token("SEMICOLON", ";")], meta=copy.deepcopy(node.meta))
                                           )
            elif isinstance(node, Tree) and node.data == "spplang_method_definition":
                # add function definition in struct
                baseFunctionDefinition = Tree(Token("RULE", "slang_struct_definition"), [
                                             Tree(Token("RULE","slang_pointer"), [
                                                 Tree(Token("RULE","slang_ftype"), [
                                                     Tree(Token("RULE", "slang_ptype"), [
                                                         Token("LPAR","(")]), 
                                                     Tree(Token("RULE","slang_rtype"), [
                                                         Token("__ANON__","->"), 
                                                         Token("RPAR",")")])]),
                                                 Token("STAR","*")]), 
                                             Tree(Token("RULE","slang_identifier"), [Token("__ANON__", f"{node.children[2].children[0]}")]), 
                                             Token("EQUAL", "="), 
                                             Tree(Token("RULE", "slang_reference"), [Token("AMPERSAND", "&"), Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", f"{node.children[2].children[0]}{abs(hash(node))}")])]), 
                                             Token("SEMICOLON", ";")], meta=copy.deepcopy(node.meta))
                # add parameter types to function definition type
                for param in filter(lambda x: isinstance(x,Tree), node.children[3].children):
                    baseFunctionDefinition.children[0].children[0].children[0].children.append(param.children[0])
                    baseFunctionDefinition.children[0].children[0].children[0].children.append(Token("COMMA",","))
                # remove last comma
                del baseFunctionDefinition.children[0].children[0].children[0].children[-1]
                # add return type to function definition type
                baseFunctionDefinition.children[0].children[0].children[1].children.insert(-1,node.children[1])
                # add function definition to the base struct
                baseStruct.children.insert(-1, baseFunctionDefinition)
                node.children[2].children[0] = Token("__ANON__", f"{node.children[2].children[0]}{abs(hash(node))}")
                node.data = "spplang_function_definition"
                additionalFunctions.append(node)
            elif isinstance(node, Token):
                # add token as is (like commas and semicolons)
                baseStruct.children.insert(-1, node)
            else:
                raise ValueError(f"Unexpected node: {node}")

        return [baseStruct, *additionalFunctions]

def classes(parseTree):
    if parseTree.data != "spplang_start": raise ValueError("top level insertions may be required")
    return Classes().transform(parseTree)



