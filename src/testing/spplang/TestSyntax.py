import unittest
from lark import Lark
from lark.lexer import Token
from lark.tree import Tree

from src.syntax import Production as P

from src.syntax.spplang import expression
from src.syntax.spplang import statement
from src.syntax.spplang import classDefinition
from src.syntax.spplang import lang
from src.syntax import Language



class TestSyntax(unittest.TestCase):

   def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.expressionLanguage = Lark(Language(expression).toLark())
        self.statementLanguage = Lark(Language(statement).toLark())
        self.classLanguage = Lark(Language(classDefinition).toLark())
        self.sppLanguage = lang

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
            def int64 pi;
            def int64 f(int64 x, int64 y) does return x + y;;
         ;
      """)

   def test_qualification(self):
      self.classLanguage.parse("""
      class A with 
         def int64 x; 
         def int64 getX() does return self.x;;
      ;""")

   def test_imports(self):
      self.sppLanguage.parse("""
      from "a/b/c" import F as D;
      class X with;
      """)

   def test_spplang_class(self):
      self.sppLanguage.parse("""
      from "a/b/c" import F as D;
      def void f();
      class X with;
      """)

   def test_spplang_new(self):
      self.sppLanguage.parse("""
      from "a/b/c" import F as D;
      def void f();
      class X with;
      def int64 start() does X x = new X();;
      """)



if __name__ == "__main__":
   unittest.main() 
