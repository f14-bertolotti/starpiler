from lark.visitors import v_args
from lark.tree import Tree
from lark import Token

from src.semantics.types import *
from src.utils import AppliedTransformer


class Fields(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_field_definition(self, meta, nodes):
        self.applied = True
        return Tree(Token('RULE', 'spplang_field_declaration'), [
            Token('DEF', 'def'), 
            nodes[1], 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[2].children[0].value)]), 
            Token('SEMICOLON', ';')], meta)


def fields(parseTree):
    return Fields().transform(parseTree)



