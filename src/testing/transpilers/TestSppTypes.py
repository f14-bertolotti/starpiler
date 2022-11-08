import unittest
from lark.tree           import Tree
from src.semantics.types import Double, Int64, Int32, Int8, Void, Pointer, SType, FType
from src.syntax.spplang  import lang
from src.transpilers     import addSppEndMethod
from src.transpilers     import sppTypes
from src.utils           import NodeMatcher

class Test(unittest.TestCase):

    def test_integer(self):
        tree = sppTypes(lang.parse("def int64 start() does return 1 + 12 - 1233 ;;"))
        for integer in NodeMatcher(lambda t: isinstance(t,Tree) and t.data == "spplang_integer").visit(tree):
            self.assertEqual(str(integer.meta.type), str(Int64()))
            self.assertEqual(integer.meta.type, Int64())

    def test_rational(self):
        tree = sppTypes(lang.parse("def int64 start() does return 1.0 + 12.12 - 1233.333 ;;"))
        for rational in NodeMatcher(lambda t: isinstance(t,Tree) and t.data == "spplang_rational").visit(tree):
            self.assertEqual(str(rational.meta.type), str(Double()))
            self.assertEqual(rational.meta.type, Double())

    def test_global_assignement(self):
        treeAndRes = [(sppTypes(lang.parse("def double x = 1233.333;")), Double()),
                      (sppTypes(lang.parse("def void f0(int64 x, int64 y) does return;; def (int64, int64 -> void)* f = &f0;")), Pointer(FType([Int64(), Int64()], Void()))),]

        for tree, res in treeAndRes:
            for tree in NodeMatcher(lambda t: isinstance(t,Tree) and t.data == "spplang_global_assignement").visit(tree):
                self.assertEqual(str(tree.meta.type), str(res))
                self.assertEqual(tree.meta.type, res)


    def test_function_definition(self):
        treeAndRes = [(sppTypes(lang.parse("def double  f() does return 1.0 + 12.12 - 1233.333;;"))      , FType([], Double())),
                      (sppTypes(lang.parse("def void    f(int64 x, int64 y) does return;;"))             , FType([Int64(), Int64()], Void())),
                      (sppTypes(lang.parse("def double* f(int64 x, double y) does return 0 as int8*;;")) , FType([Int64(), Double()], Pointer(Double())))]

        for tree, res in treeAndRes:
            for function in NodeMatcher(lambda t: isinstance(t,Tree) and t.data == "spplang_function_definition").visit(tree):
                self.assertEqual(str(function.meta.type), str(res))
                self.assertEqual(function.meta.type, res)

    def test_function_declaration(self):
        treeAndRes = [(sppTypes(lang.parse("def double f(int64, int64);"))        , FType ([Int64(), Int64()], Double())),
                      (sppTypes(lang.parse("def int8*  f(int8*, ...);"))          , FType ([Pointer(Int8())], Pointer(Int8()), vararg=True)),
                      (sppTypes(lang.parse("def void   f(int64, int64, int8*);")) , FType ([Int64(), Int64(), Pointer(Int8())], Void()))]

        for tree, res in treeAndRes:
           for function in NodeMatcher(lambda t: isinstance(t,Tree) and t.data == "spplang_function_definition").visit(tree):
               self.assertEqual(str(function.meta.type), str(res))
               self.assertEqual(function.meta.type, res)

    def test_class_definition(self):
        restype0        = SType ("X",{"x":Int64(), "y":Int64()})
        restype1        = SType ("X",{"x":Int64(), "y":Int64()})
        restype1["end"] = Pointer(FType([Pointer(restype1)], Void()))
        restype2        = SType ("X",{})
        restype2["x"]   = Pointer(restype2)
        treeAndRes = [(sppTypes(lang.parse("class X with def int64 x; def int64 y;;"))                  , restype0),
                      (sppTypes(addSppEndMethod(lang.parse("class X with def int64 x; def int64 y;;"))) , restype1),
                      (sppTypes(lang.parse("class X with def X* x;;"))                                  , restype2)]
        for tree, res in treeAndRes:
            for classtree in NodeMatcher(lambda t: isinstance(t,Tree) and t.data == "spplang_class").visit(tree):
                self.assertEqual(str(classtree.meta.type), str(res))
                self.assertEqual(classtree.meta.type, res)

    def test_class_import(self):
        restype0          = SType("Y",{"a":Int64(),"b":Int64()})
        restype0["start"] = Pointer(FType([Pointer(restype0), Int64(), Int64()], Pointer(restype0)))
        restype0["sum"]   = Pointer(FType([Pointer(restype0)], Int64()))

        treeAndRes = [(sppTypes(addSppEndMethod(lang.parse("from \"src/testing/spplang/programs/class.spp\" import X as Y;"))), restype0)]
        for tree, res in treeAndRes:
            for importtree in NodeMatcher(lambda t: isinstance(t,Tree) and t.data == "spplang_import").visit(tree):
                self.assertEqual(str(importtree.meta.type), str(res))
                self.assertEqual(importtree.meta.type, res)

      
     
if __name__ == "__main__":
    unittest.main()   
