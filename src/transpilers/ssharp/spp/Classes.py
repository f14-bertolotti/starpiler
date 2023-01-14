from lark.visitors import v_args
from lark.tree import Tree
from lark import Token

from src.semantics.types import *
from src.utils import AppliedTransformer


class Classes(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_class_definition(self, meta, nodes):
        self.applied = True
        meta.type = meta.type.base
        return Tree(Token('RULE', 'spplang_start'), [
            Tree(Token('RULE', 'spplang_class'), [
                Token('CLASS', 'class'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[1].children[0].value)]), 
                Token('WITH', 'with'), 
                *nodes[3:-1],
                Token('SEMICOLON', ';')])], meta)


def classes(parseTree):
    return Classes().transform(parseTree)



