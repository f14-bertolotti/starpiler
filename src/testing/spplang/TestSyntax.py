import unittest
from lark import Lark
from lark.lexer import Token
from lark.tree import Tree

from src.syntax import Production as P

from src.syntax.spplang import expression
from src.syntax.spplang import statement
from src.syntax import Language


class TestSyntax(unittest.TestCase):

   def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.expressionLanguage = Lark(Language(expression).toLark())
        self.statementLanguage = Lark(Language(statement).toLark())
   def test(self):pass

 
   def test_expression1(self):
      self.assertEqual(self.expressionLanguage.parse("x"), 
                       Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_6", "x")]))

   def test_expression2(self):
      self.assertEqual(self.expressionLanguage.parse("x + 5 * z"), 
                       Tree(Token("RULE", "spplang_addition"), [Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_6", "x")]), Tree(Token("RULE", "spplang_multiplication"), [Tree(Token("RULE", "spplang_integer"), [Token("__ANON_5", "5")]), Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_6", "z")])])]))

   def test_statement1(self):
      self.assertEqual(self.statementLanguage.parse("atype x = [1,2,3];"), Tree(Token("RULE", "spplang_declaration_assignment"), [Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_0", "atype")]), Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_0", "x")]), Tree(Token("RULE", "spplang_array"), [Tree(Token("RULE", "spplang_integer"), [Token("__ANON_6", "1")]), Tree(Token("RULE", "spplang_integer"), [Token("__ANON_6", "2")]), Tree(Token("RULE", "spplang_integer"), [Token("__ANON_6", "3")])])]))

   def test_statement2(self):
      self.assertEqual(self.statementLanguage.parse("if y > 0 do &y = y + 1; &y + 1 = 2;;"),Tree(Token("RULE", "spplang_ifthen"), [Tree(Token("RULE", "spplang_greater"), [Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_0", "y")]), Tree(Token("RULE", "spplang_integer"), [Token("__ANON_6", "0")])]), Tree(Token("RULE", "spplang_block"), [Tree(Token("RULE", "spplang_assignement"), [Tree(Token("RULE", "spplang_reference"), [Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_0", "y")])]), Tree(Token("RULE", "spplang_addition"), [Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_0", "y")]), Tree(Token("RULE", "spplang_integer"), [Token("__ANON_6", "1")])])]), Tree(Token("RULE", "spplang_assignement"), [Tree(Token("RULE", "spplang_addition"), [Tree(Token("RULE", "spplang_reference"), [Tree(Token("RULE", "spplang_identifier"), [Token("__ANON_0", "y")])]), Tree(Token("RULE", "spplang_integer"), [Token("__ANON_6", "1")])]), Tree(Token("RULE", "spplang_integer"), [Token("__ANON_6", "2")])])])]))

if __name__ == "__main__":
   unittest.main() 
