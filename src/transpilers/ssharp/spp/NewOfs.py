from lark.visitors import v_args
from lark import Tree, Token

from src.semantics.types import *
from src.utils import AppliedTransformer


class NewOfs(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_new_of(self, meta, nodes):
        self.applied = True

        return Tree(Token('RULE', 'spplang_cast'), [
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
                Token('STAR', '*')])])

malloc = Tree(Token('RULE', 'spplang_import'), [Token('FROM', 'from'), Tree(Token('RULE', 'spplang_string'), [Token('__ANON_0', '"src/testing/spplang/programs/gc/GC.spp"')]), Token('IMPORT', 'import'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', 'malloc')]), Token('AS', 'as'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', '__malloc__')]), Token('SEMICOLON', ';')])

def newofs(parseTree):
    parseTree = NewOfs().transform(parseTree)
    parseTree.children.insert(0, malloc)
    return parseTree



