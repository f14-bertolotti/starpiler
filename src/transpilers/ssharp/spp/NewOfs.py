from lark.visitors import Transformer
from lark import Tree, Token
from src.transpilers.ssharp.spp.Utils import *
from src.utils import NotAppliedException
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


class NewOfs(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.starters = []

    def reset(self):
        self.starters.clear()
        return self

    def transform(self, *args, **kwargs):
        return super().transform(*args, **kwargs), self.starters

    def ssharplang_new_of(self, nodes):
        self.starters.append(getStartAll(nodes[3], nodes[5]))
        return Tree(Token('RULE', 'spplang_function_call'), [
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
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'push')])]), 
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
                                                nodes[1],
                                                Token('STAR', '*'),
                                                Tree(Token('RULE', 'spplang_size_of'), [
                                                    Token('SIZE', 'size'), 
                                                    Token('OF', 'of'), 
                                                    nodes[3]])])]), 
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
                                nodes[1], 
                                Token('STAR', '*'),
                                Tree(Token('RULE', 'spplang_size_of'), [
                                    Token('SIZE', 'size'), 
                                    Token('OF', 'of'), 
                                    nodes[3]])])]), 
                        Token('RPAR', ')')]), 
                    Token('AS', 'as'), 
                    Tree(Token('RULE', 'spplang_pointer'), [
                        nodes[3],
                        Token('STAR', '*')])]),
                nodes[1]]), 
            Token('RPAR', ')')])

class BlockTransformer(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.newofsTransformer = NewOfs()
        self.starters = [] 
        self.classnode_index = None

    def reset(self):
        self.newofsTransformer.reset()
        self.starters.clear()
        self.classnode_index = None
        return self

    def transform(self, *args, **kwargs):
        result = super().transform(*args, **kwargs)
        # if no starter could be build, fail
        if len(self.starters) == 0: raise NotAppliedException("no ssharplang_new_of found")
        # if no ssharplang_class can be found, fail. 
        if self.classnode_index == None: raise NotAppliedException("could not find a single class node. Probably it was already translated")
        return result

    def ssharplang_start(self, nodes):
        # find first ssharplang_class index
        self.classnode_index = None
        for self.classnode_index,node in enumerate(nodes):
            if isinstance(node,Tree) and node.data == "ssharplang_class": break

        # insert starter functions before the first ssharplang_class
        for starter in self.starters:
            nodes.insert(self.classnode_index, starter)

        return Tree(Token("RULE","ssharplang_start"), nodes)

    def ssharplang_block(self, nodes):
        tree = Tree(Token("RULE","ssharplang_block"), nodes)
        tree, starters = self.newofsTransformer.reset().transform(tree)
        self.starters += starters

        # adds gc.pop() before the last statement if the last statement is a ssharplang_return
        # otherwise adds gc.pop() as the last statements
        pops = [copy.deepcopy(gcPop) for _ in starters]
        tree.children = tree.children[:-1] + pops + [tree.children[-1]] if tree.children[-1].data == "ssharplang_return" else tree.children + pops
        return tree

blockTransformer = BlockTransformer()
def newofs(parseTree):
    """ 
        translates ssharplang_new_of into &startAllInteger((auto __ = gc).push(__,
                                                                               &__memcpyn__(&__malloc__(size of TYPE * size), 
                                                                                            Integer{} as int8*, 
                                                                                            size of Integer, 
                                                                                            size), 
                                                                              size of Integer * size) as Integer* size);
        
        for each push adds a gc.pop() at the end of the respective block.

        if not already presents adds:
            - from "/tmp/tmpx4rim366" import malloc as __malloc__ ;
            - from "/tmp/tmpx4rim366" import memcpy as __memcpy__ ;
            - from "/tmp/tmpx4rim366" import memcpyn as __memcpyn__ ;

    """
    parseTree = blockTransformer.reset().transform(parseTree)
    if importMalloc  not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMalloc))
    if importMemcpy  not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMemcpy))
    if importMemcpyn not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMemcpyn))
    return parseTree


