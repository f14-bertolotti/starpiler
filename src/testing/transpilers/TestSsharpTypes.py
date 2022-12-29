import unittest

from src.syntax.ssharplang  import lang
from src.transpilers.ssharp import types
from src.semantics.types    import *

class Test(unittest.TestCase):

    def test1(self):
        program = """
        class A {
            var int64 x;
            fun (int64 -> int64) g(x) {
                int64 y = 1;
                return x + y;
            }
        }
        """
        parsed = lang.parse(program)
        typed = types(parsed)

        self.assertEqual(typed.children[0].meta.type, Object(SType("A", {"x":Int64(),"g":FType([Int64()], Int64())})))
        self.assertEqual(typed.children[0].children[3].meta.type, Int64())
        self.assertEqual(typed.children[0].children[4].meta.type, FType([Int64()],Int64()))
        self.assertEqual(typed.children[0].children[4].children[5].children[1].children[1].children[0].meta.type, Int64())
        self.assertEqual(typed.children[0].children[4].children[5].children[1].children[1].children[2].meta.type, Int64())

    def test2(self):
        program = """
        class A {
            var int64 x;
            var double y;
            fun (int64 -> double) g(x) {
                y = 1.0;
                return (x as double) + y;
            }
        }
        """
        parsed = lang.parse(program)
        typed = types(parsed)

        self.assertEqual(typed.children[0].meta.type, Object(SType("A", {"x":Int64(),"y":Double(),"g":FType([Int64()], Double())})))
        self.assertEqual(typed.children[0].children[3].meta.type, Int64())
        self.assertEqual(typed.children[0].children[4].meta.type, Double())
        self.assertEqual(typed.children[0].children[5].meta.type, FType([Int64()],Double()))
        self.assertEqual(typed.children[0].children[5].children[5].children[1].children[1].children[0].meta.type, Double())
        self.assertEqual(typed.children[0].children[5].children[5].children[1].children[1].children[2].meta.type, Double())


    def test3(self):
        program = """
        from "src/testing/ssharplang/programs/simple_class.ss" import Simple as S;
        class A {
            var int64 x;
            var double y;
            fun (int64 -> double) g(x) {
                S s = new S();
                y = 1.0;
                return (x as double) + y;
            }
        }
        """
        parsed = lang.parse(program)
        typed = types(parsed)

        self.assertEqual(typed.children[0].children[5].meta.type, Object(SType("Simple",{"x":Int64(),"init":FType([Int64()],Void()),"increment":FType([],Int64())})))
        self.assertEqual(typed.children[1].children[5].children[5].children[0].children[0].meta.type, Object(SType("Simple",{"x":Int64(),"init":FType([Int64()],Void()),"increment":FType([],Int64())})))
        self.assertEqual(typed.children[1].children[5].children[5].children[0].children[3].meta.type, SType("Simple",{"x":Int64(),"init":FType([Int64()],Void()),"increment":FType([],Int64())}))


if __name__ == "__main__":
    unittest.main()
