import unittest

from src.syntax.spplang    import lang as spplang
from src.syntax.slang      import functionCall
from src.syntax            import Language
from src.transpilers.spp.s import classAccesses, classes
from src.transpilers.spp   import types, addEndMethods
from src.utils             import Node2String, NodeRenamer
from lark                  import Lark

functionCallLang = Lark(Language(functionCall).toLark(), keep_all_tokens=True)

class Test(unittest.TestCase):

    def test_simple_class1(self):
        program = """
        class X with 
            def int64 x; 
            def X* start(X* this, int64 x, int64 y) does return this;;
            def int64 getX(X* this) does return this.x;;;

        def int64 start() does
            X* x = new X(1,2);
            x.getX();;
        """
        spp_tree = classAccesses(classes(types(addEndMethods(spplang.parse(program)))))
        s_tree   = functionCallLang.parse("(auto __ = x).getX(__)");

        NodeRenamer(lambda x: f"s{x[3:]}" if x.startswith("spplang_") else x).visit(spp_tree)

        self.assertEqual(Node2String().transform(s_tree), 
                         Node2String().transform(spp_tree.children[-1].children[-2].children[1].children[0]))
        
 
    def test_simple_class2(self):
        program = """
        class X with 
            def int64 x; 
            def X* start(X* this, int64 x, int64 y) does return this;;
            def void setX(X* this, int64 value) does this&.x = value; return;;;

        def int64 start() does
            X* x = new X(1,2);
            x.setX(10);;
        """
        spp_tree = classAccesses(classes(types(addEndMethods(spplang.parse(program)))))
        s_tree   = functionCallLang.parse("(auto __ = x).setX(__, 10)");

        NodeRenamer(lambda x: f"s{x[3:]}" if x.startswith("spplang_") else x).visit(spp_tree)

        self.assertEqual(Node2String().transform(s_tree), 
                         Node2String().transform(spp_tree.children[-1].children[-2].children[1].children[0]))
        
  
    def test_simple_static_method(self):
        program = """
        class X with 
            def int64 x; 
            def X* start(X* this, int64 x, int64 y) does return this;;
            def void foo() does return;;;

        def int64 start() does
            X* x = new X(1,2);
            x.foo();;
        """
        spp_tree = classAccesses(classes(types(addEndMethods(spplang.parse(program)))))
        s_tree   = functionCallLang.parse("x.foo()");

        NodeRenamer(lambda x: f"s{x[3:]}" if x.startswith("spplang_") else x).visit(spp_tree)

        self.assertEqual(Node2String().transform(s_tree), 
                         Node2String().transform(spp_tree.children[-1].children[-2].children[1].children[0]))
        
    def test_simple_static_method2(self):
        program = """
        class X with 
            def int64 x; 
            def X* start(X* this, int64 x, int64 y) does return this;;
            def int64 foo(int64 x, int64 y) does return x + y;;;

        def int64 start() does
            X* x = new X(1,2);
            x.foo(1,2);;
        """
        spp_tree = classAccesses(classes(types(addEndMethods(spplang.parse(program)))))
        s_tree   = functionCallLang.parse("x.foo(1,2)");

        NodeRenamer(lambda x: f"s{x[3:]}" if x.startswith("spplang_") else x).visit(spp_tree)

        self.assertEqual(Node2String().transform(s_tree), 
                         Node2String().transform(spp_tree.children[-1].children[-2].children[1].children[0]))


     
if __name__ == "__main__":
    unittest.main()   
