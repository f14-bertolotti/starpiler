from lark.visitors import v_args
from lark import Tree, Token

from src.semantics.types import *
from src.utils import AppliedTransformer


def p(x): print(x); return x

class News(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_new(self, meta, nodes):
        self.applied = True

        return p(Tree(Token('RULE', 'spplang_function_call'), [
            Tree(Token('RULE', 'spplang_struct_access'), [
                Tree(Token('RULE', 'spplang_round_parenthesized'), [
                    Token('LPAR', '('), 
                    Tree(Token('RULE', 'spplang_auto_assignement'), [
                        Token('AUTO', 'auto'), 
                        Tree(Token('RULE', 'spplang_identifier'), [
                            Token('__ANON_1', '__')]), 
                        Token('EQUAL', '='), 
                        Tree(Token('RULE', 'spplang_cast'), [
                            Tree(Token('RULE', 'spplang_function_call'), [
                                Tree(Token('RULE', 'spplang_struct_access'), [
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                                    Token('DOT', '.'), 
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'push')])]), 
                                Token('LPAR', '('), 
                                Tree(Token('RULE', 'spplang_expression_sequence'), [
                                    Tree(Token('RULE', 'spplang_function_call'), [
                                        Tree(Token('RULE', 'spplang_reference'), [
                                            Token('AMPERSAND', '&'), 
                                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__memcpy__')])]), 
                                        Token('LPAR', '('), 
                                        Tree(Token('RULE', 'spplang_expression_sequence'), [
                                            Tree(Token('RULE', 'spplang_function_call'), [
                                                Tree(Token('RULE', 'spplang_reference'), [
                                                    Token('AMPERSAND', '&'), 
                                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__malloc__')])]), 
                                                Token('LPAR', '('), 
                                                Tree(Token('RULE', 'spplang_expression_sequence'), [
                                                    Tree(Token('RULE', 'spplang_size_of'), [
                                                        Token('SIZE', 'size'), 
                                                        Token('OF', 'of'), 
                                                        Tree(Token('RULE', 'spplang_tname'), [nodes[1]])])]), 
                                                Token('RPAR', ')')]), 
                                            Token('COMMA', ','), 
                                            Tree(Token('RULE', 'spplang_cast'), [
                                                Tree(Token('RULE', 'spplang_struct_value'), [
                                                    nodes[1], 
                                                    Token('LBRACE', '{'), 
                                                    Token('RBRACE', '}')]), 
                                                Token('AS', 'as'), 
                                                Tree(Token('RULE', 'spplang_pointer'), [
                                                    Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), 
                                                    Token('STAR', '*')])]), 
                                            Token('COMMA', ','), 
                                            Tree(Token('RULE', 'spplang_size_of'), [
                                                Token('SIZE', 'size'), 
                                                Token('OF', 'of'), 
                                                Tree(Token('RULE', 'spplang_tname'), [nodes[1]])])]), 
                                        Token('RPAR', ')')]),
                                Token('COMMA',','),
                                Tree(Token('RULE', 'spplang_size_of'), [
                                    Token('SIZE', 'size'), 
                                    Token('OF', 'of'), 
                                    Tree(Token('RULE', 'spplang_tname'), [nodes[1]])])]), 
                                Token('RPAR', ')')]), 
                            Token('AS', 'as'), 
                            Tree(Token('RULE', 'spplang_pointer'), [
                                Tree(Token('RULE', 'spplang_tname'), [
                                    nodes[1]]), 
                                Token('STAR', '*')])])]), 
                    Token('RPAR', ')')]), 
                Token('DOT', '.'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'start')])]), 
            Token('LPAR', '('), 
            nodes[3], 
            Token('RPAR', ')')]))


malloc = Tree(Token('RULE', 'spplang_import'), [Token('FROM', 'from'), Tree(Token('RULE', 'spplang_string'), [Token('__ANON_0', '"src/testing/spplang/programs/gc/GC.spp"')]), Token('IMPORT', 'import'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', 'malloc')]), Token('AS', 'as'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__malloc__')]), Token('SEMICOLON', ';')])
memcpy = Tree(Token('RULE', 'spplang_import'), [Token('FROM', 'from'), Tree(Token('RULE', 'spplang_string'), [Token('__ANON_0', '"src/testing/spplang/programs/gc/GC.spp"')]), Token('IMPORT', 'import'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', 'memcpy')]), Token('AS', 'as'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__memcpy__')]), Token('SEMICOLON', ';')])


def news(parseTree):
    parseTree = News().transform(parseTree)
    parseTree.children.insert(0, malloc)
    parseTree.children.insert(0, memcpy)
    return parseTree



