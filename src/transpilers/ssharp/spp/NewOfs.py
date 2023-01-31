from lark.visitors import Transformer
from lark import Tree, Token
from src.transpilers.ssharp.spp.Utils import *
from src.utils import NotAppliedException
import copy

def get_new_assignement(name, size, typ):
    """ returns _x_ = __malloc__(_size_ * size of int8*);"""
    return [
        Tree(Token('RULE', 'spplang_stmt_expr'), [
            Tree(Token('RULE', 'spplang_declaration_assignment'), [
                Tree(Token('RULE', 'spplang_int64'), [Token('INT64', 'int64')]), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '_size_')]), 
                Token('EQUAL', '='), 
                size]), 
            Token('SEMICOLON', ';')]),

        Tree(Token('RULE', 'spplang_stmt_expr'), [
            Tree(Token('RULE', 'spplang_auto_assignement'), [
                Token('AUTO', 'auto'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', name)]), 
                Token('EQUAL', '='), 
                Tree(Token('RULE', 'spplang_cast'), [
                    Tree(Token('RULE', 'spplang_function_call'), [
                        Tree(Token('RULE', 'spplang_struct_access'), [
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                            Token('DOT', '.'), 
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gcmalloc')])]), 
                        Token('LPAR', '('), 
                        Tree(Token('RULE', 'spplang_expression_sequence'), [
                            Tree(Token('RULE', 'spplang_multiplication'), [
                                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '_size_')]), 
                                Token('STAR', '*'), 
                                Tree(Token('RULE', 'spplang_size_of'), [
                                    Token('SIZE', 'size'), 
                                    Token('OF', 'of'), 
                                    Tree(Token('RULE', 'spplang_pointer'), [
                                        Tree(Token('RULE', 'spplang_int8'), [
                                            Token('INT8', 'int8')]), 
                                        Token('STAR', '*')])])])]), 
                        Token('RPAR', ')')]),
                    Token('AS', 'as'),
                    Tree(Token('RULE', 'spplang_pointer'), [
                        Tree(Token('RULE', 'spplang_pointer'), [
                            Tree(Token('RULE', 'spplang_tname'), [typ]), 
                            Token('STAR', '*')]), 
                        Token('STAR', '*')])
                ])]), 
            Token('SEMICOLON', ';')])
    ]

def get_while_init(name, typ, params):
    return [
        Tree(Token('RULE', 'spplang_stmt_expr'), [
            Tree(Token('RULE', 'spplang_declaration_assignment'), [
                Tree(Token('RULE', 'spplang_int64'), [Token('INT64', 'int64')]), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'i')]), 
                Token('EQUAL', '='), 
                Tree(Token('RULE', 'spplang_integer'), [Token('__ANON__', '0')])]), 
            Token('SEMICOLON', ';')]), 

        Tree(Token('RULE', 'spplang_while'), [
            Token('WHILE', 'while'), 
            Tree(Token('RULE', 'spplang_less'), [
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'i')]), 
                Token('LESSTHAN', '<'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '_size_')])]), 
            Token('DO', 'do'), 
            Tree(Token('RULE', 'spplang_block'), [
                Tree(Token('RULE', 'spplang_stmt_expr'), [
                    Tree(Token('RULE', 'spplang_assignement'), [
                        Tree(Token('RULE', 'spplang_indexed'), [
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', name)]), 
                            Tree(Token('RULE', 'spplang_reference_square_parenthesized'), [
                                Token('__ANON__', '&['), 
                                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_', 'i')]), 
                                Token('RSQB', ']')])]), 
                        Token('EQUAL', '='), 
                        Tree(Token('RULE', 'spplang_cast'), [
                            Tree(Token('RULE', 'spplang_function_call'), [
                                Tree(Token('RULE', 'spplang_struct_access'), [
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                                    Token('DOT', '.'), 
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gcmemcpy')])]), 
                                Token('LPAR', '('), 
                                Tree(Token('RULE', 'spplang_expression_sequence'), [
                                    Tree(Token('RULE', 'spplang_size_of'), [
                                        Token('SIZE', 'size'), 
                                        Token('OF', 'of'), 
                                        Tree(Token('RULE', 'spplang_tname'), [typ])]), 
                                    Token('COMMA', ','), 
                                    Tree(Token('RULE', 'spplang_cast'), [
                                        Tree(Token('RULE', 'spplang_struct_value'), [
                                            typ, 
                                            Token('LBRACE', '{'), 
                                            Token('RBRACE', '}')]),
                                    Token('AS','as'),
                                    Tree(Token('RULE', 'spplang_pointer'), [
                                        Tree(Token('RULE', 'spplang_int8'), [
                                            Token('INT8', 'int8')]), 
                                        Token('STAR', '*')])
                                    ])]), 
                                Token('RPAR', ')')]),
                        Token('AS','as'),
                        Tree(Token('RULE', 'spplang_pointer'), [
                            Tree(Token('RULE', 'spplang_tname'), [typ]), 
                            Token('STAR', '*')])])]), 
                    Token('SEMICOLON', ';')]), 
                Tree(Token('RULE', 'spplang_stmt_expr'), [
                        Tree(Token('RULE', 'spplang_function_call'), [
                            Tree(Token('RULE', 'spplang_struct_access'), [
                                Tree(Token('RULE', 'spplang_indexed'), [
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', name)]), 
                                    Tree(Token('RULE', 'spplang_square_parenthesized'), [
                                        Token('LSQB', '['), 
                                        Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'i')]), 
                                        Token('RSQB', ']')])]), 
                                Token('DOT', '.'), 
                                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'start')])]), 
                            Token('LPAR', '('), 
                            *params,
                            Token('RPAR', ')')]), 
                        Token('SEMICOLON', ';')]),
                copy.deepcopy(gcPop),
                Tree(Token('RULE', 'spplang_stmt_expr'), [
                    Tree(Token('RULE', 'spplang_assignement'), [
                        Tree(Token('RULE', 'spplang_reference'), [
                            Token('AMPERSAND', '&'), 
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'i')])]), 
                        Token('EQUAL', '='), 
                        Tree(Token('RULE', 'spplang_addition'), [
                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'i')]), 
                            Token('PLUS', '+'), 
                            Tree(Token('RULE', 'spplang_integer'), [Token('__ANON__', '1')])])]), 
                    Token('SEMICOLON', ';')])]), 
            Token('SEMICOLON', ';')])
    ]


class NewOfs(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assignements = list()

    def reset(self):
        self.assignements.clear()
        return self

    def transform(self, *args, **kwargs):
        return super().transform(*args, **kwargs), self.assignements

    def ssharplang_new_of(self, nodes):
        name = f"_{len(self.assignements)}_"
        self.assignements += get_new_assignement(name, nodes[1], nodes[3].children[0])
        self.assignements += get_while_init(name, nodes[3].children[0], [nodes[5]] if len(nodes) == 7 else [])
        return Tree(Token("RULE","spplang_identifier"), [Token("__ANON__",name)])

class BlockTransformer(Transformer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.newOfs = NewOfs()
        self.applied = False

    def reset(self):
        self.applied = False
        return self

    def transform(self, *args, **kwargs):
        result = super().transform(*args, **kwargs)
        if not self.applied: raise NotAppliedException("BlockTransformer not applied");
        return result

    def ssharplang_start(self, nodes):
        if importgc not in nodes: nodes.insert(0, importgc)
        return Tree(Token("RULE","ssharplang_start"), nodes)

    def ssharplang_block(self, nodes):
        newnodes = list()
        future_pops = 0
        for node in nodes:
            node, ass = self.newOfs.reset().transform(node)
            future_pops += len(ass) // 4
            newnodes = newnodes + ass + [node]

        if future_pops > 0: self.applied = True
    
        return Tree(Token("RULE", "ssharplang_pop_block"), newnodes + [future_pops])

    
blockTransformer = BlockTransformer()
def newofs(parseTree):
    return blockTransformer.reset().transform(parseTree)


