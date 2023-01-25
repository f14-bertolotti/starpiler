from lark.visitors import v_args
from lark import Tree, Token

from src.semantics.types import *
from src.utils import AppliedTransformer
from src.transpilers.ssharp.spp.Utils import *
import copy


def getStartAll(tname, params):
    return \
    Tree(Token('RULE', 'spplang_function_definition'), [
        Token('DEF', 'def'), 
        Tree(Token('RULE', 'spplang_pointer'), [
            tname, 
            Token('STAR', '*')]), 
        Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', f'startAll{tname.children[0].children[0].value}')]), 
        Tree(Token('RULE', 'spplang_parameter_seq_def'), [
            Token('LPAR', '('), 
            Tree(Token('RULE', 'spplang_parameter_definition'), [
                Tree(Token('RULE', 'spplang_pointer'), [
                    tname, 
                    Token('STAR', '*')]), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'ptr')])]), 
            Token('COMMA', ','), 
            Tree(Token('RULE', 'spplang_parameter_definition'), [
                Tree(Token('RULE', 'spplang_int64'), [Token('INT64', 'int64')]), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'size')])]), 
            Token('RPAR', ')')]), 
        Token('DOES', 'does'), 
        Tree(Token('RULE', 'spplang_block'), [
            Tree(Token('RULE', 'spplang_while'), [
                Token('WHILE', 'while'), 
                Tree(Token('RULE', 'spplang_not_equal'), [
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'size')]), 
                    Token('__ANON__', '!='), 
                    Tree(Token('RULE', 'spplang_integer'), [Token('__ANON__', '0')])]), 
                Token('DO', 'do'), 
                Tree(Token('RULE', 'spplang_block'), [
                    Tree(Token('RULE', 'spplang_stmt_expr'), [
                        Tree(Token('RULE', 'spplang_assignement'), [
                            Tree(Token('RULE', 'spplang_reference'), [
                                Token('AMPERSAND', '&'), 
                                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'size')])]), 
                            Token('EQUAL', '='), 
                            Tree(Token('RULE', 'spplang_subtraction'), [
                                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'size')]), 
                                Token('MINUS', '-'), 
                                Tree(Token('RULE', 'spplang_integer'), [Token('__ANON__', '1')])])]), 
                        Token('SEMICOLON', ';')]),
                    Tree(Token('RULE', 'spplang_stmt_expr'), [
                        Tree(Token('RULE', 'spplang_function_call'), [
                            Tree(Token('RULE', 'spplang_struct_access'), [
                                Tree(Token('RULE', 'spplang_indexed'), [
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'ptr')]), 
                                    Tree(Token('RULE', 'spplang_reference_square_parenthesized'), [
                                        Token('__ANON__', '&['), 
                                        Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'size')]), 
                                        Token('RSQB', ']')])]), 
                                Token('DOT', '.'), 
                                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'start')])]), 
                            Token('LPAR', '('), 
                            params, 
                            Token('RPAR', ')')]), 
                        Token('SEMICOLON', ';')]),]), 
                Token('SEMICOLON', ';')]), 
            Tree(Token('RULE', 'spplang_return'), [
                Token('RETURN', 'return'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'ptr')]), 
                Token('SEMICOLON', ';')])]),  
        Token('SEMICOLON', ';')])


class NewOfs(AppliedTransformer):

    def __init__(self, *args, isMain=True, **kwargs):
        self.isMain = isMain
        self.starters = []
        super().__init__(*args, **kwargs)

    @v_args(meta=True)
    def ssharplang_start(self, meta, nodes):
        for starter in self.starters:
            pass
            #import rich
            #rich.print(starter)
            nodes.insert(5, starter) # TODO FIX
        return Tree(Token("RULE","ssharplang_start"), nodes, meta)

    @v_args(meta=True)
    def ssharplang_new_of(self, meta, nodes):
        self.applied = True
        self.starters.append(getStartAll(nodes[3], nodes[5]))

        ret = Tree(Token('RULE', 'spplang_function_call'), [
            Tree(Token('RULE', 'spplang_reference'), [
                Token('AMPERSAND', '&'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', f'startAll{nodes[3].children[0].children[0].value}')])]), 
            Token('LPAR', '('), 
            Tree(Token('RULE', 'spplang_expression_sequence'), [

                Tree(Token('RULE', 'spplang_cast'), [
                    Tree(Token('RULE', 'spplang_function_call'), [
                        Tree(Token('RULE', 'spplang_struct_access'), [
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                            Token('DOT', '.'), 
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'pushNoRoot')])]), 
                        Token('LPAR', '('), 
                        Tree(Token('RULE', 'spplang_expression_sequence'), [
                            Tree(Token('RULE', 'spplang_function_call'), [
                                Tree(Token('RULE', 'spplang_reference'), [
                                    Token('AMPERSAND', '&'), 
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__memcpyn__')])]), 
                                Token('LPAR', '('), 
                                Tree(Token('RULE', 'spplang_expression_sequence'), [
                                    Tree(Token('RULE', 'spplang_function_call'), [
                                        Tree(Token('RULE', 'spplang_reference'), [
                                            Token('AMPERSAND', '&'), 
                                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__malloc__')])]), 
                                        Token('LPAR', '('), 
                                        Tree(Token('RULE', 'spplang_expression_sequence'), [
                                            Tree(Token('RULE', 'spplang_multiplication'), [
                                                Tree(Token('RULE', 'spplang_size_of'), [
                                                    Token('SIZE', 'size'), 
                                                    Token('OF', 'of'), 
                                                    nodes[3]]), 
                                                Token('STAR', '*'), 
                                                nodes[1]])]), 
                                        Token('RPAR', ')')]), 
                                    Token('COMMA', ','), 
                                    Tree(Token('RULE', 'spplang_cast'), [
                                        Tree(Token('RULE', 'spplang_struct_value'), [
                                            nodes[3].children[0], 
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
                                        nodes[3]]), 
                                    Token('COMMA', ','), 
                                    nodes[1]]), 
                                Token('RPAR', ')')]), 
                            Token('COMMA', ','), 
                            Tree(Token('RULE', 'spplang_multiplication'), [
                                Tree(Token('RULE', 'spplang_size_of'), [
                                    Token('SIZE', 'size'), 
                                    Token('OF', 'of'), 
                                    nodes[3]]), 
                                Token('STAR', '*'), 
                                nodes[1]])]), 
                        Token('RPAR', ')')]), 
                    Token('AS', 'as'), 
                    Tree(Token('RULE', 'spplang_pointer'), [
                        nodes[3],
                        Token('STAR', '*')])]),

                nodes[1]]), 
            Token('RPAR', ')')])
        import rich
        rich.print(ret)
        return ret


        

def mainNewofs(parseTree):
    parseTree = NewOfs(isMain=True).transform(parseTree)
    parseTree.children.insert(0, malloc)
    return parseTree

def newofs(parseTree):
    parseTree = NewOfs(isMain=False).transform(parseTree)
    if importMalloc  not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMalloc))
    if importMemcpy  not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMemcpy))
    if importMemcpyn not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMemcpyn))
    return parseTree


