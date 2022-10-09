import unittest

from src.syntax import Language   as L
from src.syntax import Production as P
from src.syntax import Rule       as R
from src.syntax import Terminal   as T

from src.syntax import getChangePrefixVisitor
from src.syntax import getClonerVisitor

class TestBasics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        x = P(name="slang_x", rules=[R(T("X")), R(T("Y"))])
        y = P(name="slang_y", rules=[x, R(T("("), x, T(")")), R(x,x)])
        z = P(name="slang_z", rules=[y])
        z.append(R(y,z))
        self.lang = L(z)

    def test_changePrefixVisitor(self):
        lang0 = self.lang.visit(getClonerVisitor(self.lang))
        lang1 = self.lang.visit(getClonerVisitor(self.lang))\
                         .visit(getChangePrefixVisitor("slang_","spplang_"))
        self.assertEqual(lang0.toLark().replace("slang_","spplang_"), lang1.toLark())

    def test_clonerVisitor(self):
        self.assertTrue(self.lang is self.lang)
        self.assertFalse(self.lang is self.lang.visit(getClonerVisitor(self.lang)))
        self.assertEqual(self.lang.toLark(), self.lang.visit(getClonerVisitor(self.lang)).toLark())
        
if __name__ == "__main__":
    unittest.main()
