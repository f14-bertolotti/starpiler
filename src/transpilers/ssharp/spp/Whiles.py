from lark import Tree, Token
from src.utils import AppliedTransformer

class Whiles(AppliedTransformer):
    
    def reset(self):
        self.applied = False
        return self

    def ssharplang_while(self, nodes):
        self.applied = True
        return Tree(Token('RULE', 'spplang_while'), [
            Token('WHILE', 'while'), 
            nodes[2], 
            Token('DO', 'do'), 
            nodes[5], 
            Token('SEMICOLON', ';')])

whilesTransformer = Whiles()
def whiles(parseTree):
    return whilesTransformer.reset().transform(parseTree)
