from lark import Tree, Token

from src.utils import AppliedTransformer

class Ifs(AppliedTransformer):
    def reset(self):
        self.applied = False
        return self

    def ssharplang_ifthen(self, nodes):
        self.applied = True
        return \
        Tree(Token('RULE', 'spplang_ifthen'), [
            Token('IF', 'if'), 
            nodes[2], 
            Token('DO', 'do'), 
            nodes[5], 
            Token('SEMICOLON', ';')]) 

transformer= Ifs()
def ifs(parseTree):
    return transformer.reset().transform(parseTree)
