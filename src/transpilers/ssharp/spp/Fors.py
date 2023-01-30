from lark import Tree, Token
from src.utils import AppliedTransformer

class Fors(AppliedTransformer):
    """
        trsform the for loop in ssharp:
            for i from expr {block}

            into the spplang while:

            auto i = 0; 
            while i < expr do 
                block; 
                i = i + 1;
            ;
    """
    
    def reset(self):
        self.applied = False
        return self

    def __default__(self, data, children, meta):
        return Tree(data, [node for child in children for node in (child if isinstance(child, list) else [child])], meta)

    def ssharplang_for(self, nodes):
        self.applied = True

        return [
            Tree(Token('RULE', 'spplang_stmt_expr'), [
                Tree(Token('RULE', 'spplang_auto_assignement'), [
                    Token('AUTO', 'auto'), 
                    nodes[1], 
                    Token('EQUAL', '='), 
                    Tree(Token('RULE', 'spplang_integer'), [Token('__ANON__', '0')])]), 
                Token('SEMICOLON', ';')]),
        
            Tree(Token('RULE', 'spplang_while'), [
                Token('WHILE', 'while'), 
                Tree(Token('RULE', 'spplang_less'), [
                    nodes[1], 
                    Token('LESSTHAN', '<'), 
                    nodes[3]]), 
                Token('DO', 'do'), 
                Tree(Token('RULE', 'spplang_block'), [
                    nodes[5],
                    Tree(Token('RULE', 'spplang_stmt_expr'), [
                        Tree(Token('RULE', 'spplang_assignement'), [
                            Tree(Token('RULE', 'spplang_reference'), [
                                Token('AMPERSAND', '&'), 
                                nodes[1]]), 
                            Token('EQUAL', '='), 
                            Tree(Token('RULE', 'spplang_addition'), [
                                nodes[1], 
                                Token('PLUS', '+'), 
                                Tree(Token('RULE', 'spplang_integer'), [
                                    Token('__ANON__', '1')])])]), 
                        Token('SEMICOLON', ';')])]), 
                Token('SEMICOLON', ';')])
        ]




forsTransformer = Fors()
def fors(parseTree):
    return forsTransformer.reset().transform(parseTree)

