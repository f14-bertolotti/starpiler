from lark.visitors import v_args
from lark import Tree, Token

from src.semantics.types import *
from src.utils import AppliedTransformer

from src.transpilers.ssharp.spp.Utils import importMalloc, importMemcpy


class News(AppliedTransformer):

    def __init__(self, *args, isMain=True, **kwargs):
        self.isMain = isMain
        super().__init__(*args, **kwargs)

    @v_args(meta=True)
    def ssharplang_new(self, meta, nodes):
        self.applied = True

        return \
        Tree(Token('RULE', 'spplang_function_call'), [
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
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'push' if self.isMain else 'pushNoRoot')])]), 
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
            Token('RPAR', ')')])


def mainNews(parseTree):
    parseTree = News(isMain=True).transform(parseTree)
    return parseTree

def news(parseTree):
    parseTree = News(isMain=False).transform(parseTree)
    if importMalloc not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMalloc))
    if importMemcpy not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMemcpy))
    return parseTree



