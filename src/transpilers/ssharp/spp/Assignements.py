from lark.visitors import v_args
from lark.tree import Tree
from lark import Token

from src.utils import AppliedTransformer

from src.semantics.types import Object, Pointer

class Assignements(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_assignement(self, meta, nodes):

        meta.type = Pointer(meta.type.base if isinstance(meta.type, Object) else meta.type)

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

        return Tree(Token("RULE", "spplang_assignements"), nodes, meta)

def assignements(parseTree) -> Tree:
    return Assignements().transform(parseTree)
