import unittest

from src.syntax.spplang import lang as spplang
from src.syntax.slang   import lang as slang
from src.transpilers    import sppTypes, addSppEndMethod, sppClassesToSStruct
from src.utils          import Node2String, NodeRenamer, NodeMatcher
from lark.visitors      import Visitor
from lark.tree          import Tree

class Test(unittest.TestCase):

    def test_simple_class(self):
        program = "class X with def int64 x; def int64 y; def X* start(X* this, int64 x, int64 y) does return this;;;"
        tree0 = sppClassesToSStruct(addSppEndMethod(sppTypes(spplang.parse(program))))
        tree1 = sppClassesToSStruct(sppTypes(addSppEndMethod(spplang.parse(program))))
        renamer = NodeRenamer(lambda x: x.replace("spplang", "slang"))
        renamer.visit(tree0)
        renamer.visit(tree1)

        resTree = slang.parse("struct X with int64 x; int64 y; (X*, int64, int64 -> X*)* start = &_1_start; (X* -> void)* end = &_2_end;;").children[0]

        matches0 = NodeMatcher(lambda x:isinstance(x,Tree) and x.data == "slang_struct").visit(tree0)[0]
        matches1 = NodeMatcher(lambda x:isinstance(x,Tree) and x.data == "slang_struct").visit(tree1)[0]
        self.assertEqual(Node2String().transform(matches0), Node2String().transform(matches1))
        self.assertEqual(Node2String().transform(resTree), Node2String().transform(matches1))
      
    def test_rec_class(self):
        program = "class X with def int64 x; def int64 y; def X* rec; def X* start(X* this, int64 x, int64 y, X* rec) does return this;;;"
        tree0 = sppClassesToSStruct(addSppEndMethod(sppTypes(spplang.parse(program))))
        tree1 = sppClassesToSStruct(sppTypes(addSppEndMethod(spplang.parse(program))))
        renamer = NodeRenamer(lambda x: x.replace("spplang", "slang"))
        renamer.visit(tree0)
        renamer.visit(tree1)

        resTree = slang.parse("struct X with int64 x; int64 y; X* rec;(X*, int64, int64, X* -> X*)* start = &_1_start; (X* -> void)* end = &_2_end;;").children[0]

        matches0 = NodeMatcher(lambda x:isinstance(x,Tree) and x.data == "slang_struct").visit(tree0)[0]
        matches1 = NodeMatcher(lambda x:isinstance(x,Tree) and x.data == "slang_struct").visit(tree1)[0]
        self.assertEqual(Node2String().transform(matches0), Node2String().transform(matches1))
        self.assertEqual(Node2String().transform(resTree), Node2String().transform(matches1))

     
if __name__ == "__main__":
    unittest.main()   
