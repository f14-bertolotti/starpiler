import unittest

from src.syntax import Language   as L
from src.syntax import Production as P
from src.syntax import Rule       as R
from src.syntax import Terminal   as T

from src.syntax import getChangePrefixVisitor

class TestBasics(unittest.TestCase):

    def test_language2string(self):

        x = P(name="slang_x", rules=[R(T("X")), R(T("Y"))])
        y = P(name="slang_y", rules=[x, R(T("("), x, T(")")), R(x,x)])
        z = P(name="slang_z", rules=[y])
        z.append(R(y,z))
        zlang = L(z)
        
        zlang.visit(getChangePrefixVisitor("slang_", "spplang_"))

        self.assertEqual(zlang.toLark().replace(" ","").replace("\n",""), """start:spplang_y|(spplang_ystart)spplang_y:spplang_x|("("spplang_x")")|(spplang_xspplang_x)spplang_x:("X")|("Y")%ignore/[\\t\\n\\f\\r]+/%ignore/#[^\\n]*/""")

