
import unittest
from src.syntax.ssharplang import lang

from lark import Token
from lark.tree import Tree

class TestSyntax(unittest.TestCase):

    def test_empty_class(self):
        program = "class A {}"
        parsed = lang.parse(program)
        self.assertEqual(parsed,
                         Tree(Token('RULE', 'ssharplang_start'), [
                             Tree(Token('RULE', 'ssharplang_class_definition'), [
                                 Token('CLASS', 'class'), 
                                 Tree(Token('RULE', 'ssharplang_identifier'), [
                                     Token('__ANON_0', 'A')]), 
                                 Token('LBRACE', '{'), 
                                 Token('RBRACE', '}')])]))
        
    def test_field(self):
        program= "class A{var int64 x; var Y y; var auto z;}"
        parsed = lang.parse(program)
        self.assertEqual(parsed,
                         Tree(Token('RULE', 'ssharplang_start'), [
                             Tree(Token('RULE', 'ssharplang_class_definition'), [
                                 Token('CLASS', 'class'), 
                                 Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'A')]), 
                                 Token('LBRACE', '{'), 
                                 Tree(Token('RULE', 'ssharplang_field_definition'), [
                                     Token('VAR', 'var'), Tree(Token('RULE', 'ssharplang_int64'), [Token('INT64', 'int64')]), Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'x')]), Token('SEMICOLON', ';')]), 
                                 Tree(Token('RULE', 'ssharplang_field_definition'), [
                                     Token('VAR', 'var'), Tree(Token('RULE', 'ssharplang_tname'), [Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'Y')])]), Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'y')]), Token('SEMICOLON', ';')]), 
                                 Tree(Token('RULE', 'ssharplang_field_definition'), [
                                     Token('VAR', 'var'), Tree(Token('RULE', 'ssharplang_tname'), [Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'auto')])]), Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'z')]), Token('SEMICOLON', ';')]), Token('RBRACE', '}')])]))

    def test_method(self):
        program = "class A{fun (int64,float -> void) f(x,y) {x+y;}}"
        parsed = lang.parse(program)
        self.assertEqual(parsed,
                         Tree(Token('RULE', 'ssharplang_start'), [
                             Tree(Token('RULE', 'ssharplang_class_definition'), [
                                 Token('CLASS', 'class'), 
                                 Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'A')]), 
                                 Token('LBRACE', '{'), 
                                 Tree(Token('RULE', 'ssharplang_method_definition'), [
                                     Token('FUN', 'fun'), 
                                     Tree(Token('RULE', 'ssharplang_ftype'), [Tree(Token('RULE', 'ssharplang_ptype'), [Token('LPAR', '('), Tree(Token('RULE', 'ssharplang_int64'), [Token('INT64', 'int64')]), Token('COMMA', ','), Tree(Token('RULE', 'ssharplang_tname'), [Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'float')])])]), Tree(Token('RULE', 'ssharplang_rtype'), [Token('__ANON_2', '->'), Tree(Token('RULE', 'ssharplang_void'), [Token('VOID', 'void')]), Token('RPAR', ')')])]), 
                                     Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'f')]), 
                                     Tree(Token('RULE', 'ssharplang_identifier_sequence'), [
                                         Token('LPAR', '('), 
                                         Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'x')]), 
                                         Token('COMMA', ','), 
                                         Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'y')]), 
                                         Token('RPAR', ')')]), 
                                     Token('LBRACE', '{'), 
                                     Tree(Token('RULE', 'ssharplang_block'), [Tree(Token('RULE', 'ssharplang_stmt_expr'), [Tree(Token('RULE', 'ssharplang_addition'), [Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'x')]), Token('PLUS', '+'), Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON_0', 'y')])]), Token('SEMICOLON', ';')])]), 
                                     Token('RBRACE', '}')]), 
                                 Token('RBRACE', '}')])]))
        
if __name__ == "__main__":
    unittest.main()

