from lark.visitors import v_args
from lark import Tree, Token

from src.semantics.types import *
from src.utils import AppliedTransformer


class Arrays(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_atype(self, meta, nodes):
        self.applied = True
        return \
        Tree(Token('RULE', 'spplang_pointer'), [
            Tree(Token('RULE', 'spplang_pointer'), [nodes[0], Token('STAR','*')]), 
            Token('STAR', '*')])


def arrays(parseTree):
    return Arrays().transform(parseTree)



