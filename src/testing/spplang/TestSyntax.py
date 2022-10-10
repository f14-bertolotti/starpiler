import unittest
from lark import Lark
from lark.lexer import Token
from lark.tree import Tree

from src.syntax import Production as P

from src.syntax.spplang import expression
from src.syntax.spplang import statement
from src.syntax.spplang import classDefinition
from src.syntax import Language


class TestSyntax(unittest.TestCase):

   def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.expressionLanguage = Lark(Language(expression).toLark())
        self.statementLanguage = Lark(Language(statement).toLark())
        self.classLanguage = Lark(Language(classDefinition).toLark())

   def test_expression1(self):
      self.expressionLanguage.parse("x")

   def test_expression2(self):
      self.expressionLanguage.parse("x + 5 * z")

   def test_statement1(self):
      self.statementLanguage.parse("atype x = [1,2,3];")

   def test_statement2(self):
      self.statementLanguage.parse("if y > 0 do &y = y + 1; &y + 1 = 2;;")

   def test_classes1(self):
      self.classLanguage.parse("""
         class A with
            def int64 pi = 3.14;
            def int64 f(int64 x, int64 y) does return x + y;;
         ;
      """)

   def test_qualification(self):
      self.classLanguage.parse("""
      class A with 
         def int64 x = 0; 
         def int64 getX() does return self.x;;
      ;""")

if __name__ == "__main__":
   unittest.main() 
