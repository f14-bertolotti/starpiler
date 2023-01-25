from lark.visitors import v_args
from lark.tree import Tree
from lark import Token

from src.utils import AppliedTransformer


class Fields(AppliedTransformer):

    def reset(self):
        self.applied = False
        return self

    def ssharplang_field_definition(self, nodes):
        self.applied = True
        return Tree(Token('RULE', 'spplang_field_declaration'), [
            Token('DEF', 'def'), 
            nodes[1], 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[2].children[0].value)]), 
            Token('SEMICOLON', ';')])

fieldsTransformer = Fields()
def fields(parseTree):
    return fieldsTransformer.reset().transform(parseTree)



