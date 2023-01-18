from lark.visitors import v_args
from lark.tree import Tree
from lark import Token

from src.utils import AppliedTransformer

from src.semantics.types import Object, Pointer

class Assignements(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_assignement(self, meta, nodes):

        meta.type = Pointer(meta.type.base if isinstance(meta.type, Object) else meta.type)
        del nodes[-1]

        if nodes[0].data == "ssharplang_identifier":
            self.applied = True
            
            nodes[0] = Tree(Token('RULE', 'spplang_reference'), [
                Token('AMPERSAND', '&'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[0].children[0].value)])], meta)

        elif nodes[0].data == "ssharplang_class_access":
            self.applied = True

            nodes[0] = Tree(Token('RULE', 'spplang_struct_ref_access'), [
                nodes[0].children[0], 
                Token('__ANON__', '&.'), 
                nodes[0].children[2]], meta)

        return Tree(Token("RULE","spplang_stmt_expr"), [Tree(Token("RULE", "spplang_assignement"), nodes, meta), Token("SEMICOLON",";")])

    @v_args(meta=True)
    def ssharplang_declaration_assignment(self, meta, nodes):
        del nodes[-1]
        return Tree(Token("RULE","spplang_stmt_expr"), [Tree(Token("RULE", "spplang_declaration_assignment"), nodes, meta), Token("SEMICOLON",";")])


    @v_args(meta=True)
    def ssharplang_auto_assignment(self, meta, nodes):
        del nodes[-1]
        return Tree(Token("RULE","spplang_stmt_expr"), [Tree(Token("RULE", "spplang_auto_assignment"), nodes, meta), Token("SEMICOLON",";")])



def assignements(parseTree) -> Tree:
    return Assignements().transform(parseTree)
