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
        self.lang.visit(getChangePrefixVisitor("slang_", "spplang_"))
        self.assertEqual(self.lang.toLark().replace(" ","").replace("\n",""), """start:spplang_y|(spplang_ystart)spplang_y:spplang_x|("("spplang_x")")|(spplang_xspplang_x)spplang_x:("X")|("Y")%ignore/[\\t\\n\\f\\r]+/%ignore/#[^\\n]*/""")

    def test_clonerVisitor(self):
        self.assertTrue(self.lang is self.lang)
        self.assertFalse(self.lang is self.lang.visit(getClonerVisitor()))
        self.assertEqual(self.lang.toLark(), self.lang.visit(getClonerVisitor()).toLark())
        self.assertEqual(self.lang.toLark(), self.lang.visit(getClonerVisitor()).toLark())
        
if __name__ == "__main__":
    unittest.main()
