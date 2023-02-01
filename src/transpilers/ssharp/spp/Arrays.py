from lark import Tree, Token

from src.semantics.types import *
from src.utils import AppliedTransformer


class Arrays(AppliedTransformer):

    def ssharplang_atype(self, nodes):
        self.applied = True
        
        # native types case
        if nodes[0].data in {"ssharplang_int64", "ssharplang_int32", "ssharplang_int8", "ssharplang_double"}:
            return Tree(Token('RULE', 'spplang_pointer'), [nodes[0], Token('STAR', '*')])

        return \
        Tree(Token('RULE', 'spplang_pointer'), [
            Tree(Token('RULE', 'spplang_pointer'), [nodes[0], Token('STAR','*')]), 
            Token('STAR', '*')])


def arrays(parseTree):
    return Arrays().transform(parseTree)



