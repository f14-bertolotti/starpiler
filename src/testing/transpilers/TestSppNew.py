import unittest

from src.syntax.spplang import lang as spplang
from src.syntax.slang   import functionCall 
from src.syntax.slang   import lang 
from src.syntax         import Language
from src.transpilers    import sppNewToS, sppTypes, addSppEndMethod, sppClassesToS
from src.utils          import Node2String, NodeRenamer, NodeMatcher
from lark.visitors      import Visitor
from lark.tree          import Tree
from lark               import Lark

functionCallLang = Lark(Language(functionCall).toLark(), keep_all_tokens=True)

class Test(unittest.TestCase):

    def test_simple_new(self):
        program = """
        class X with 
            def int64 x; 
            def int64 y; 
            def X* start(X* this, int64 x, int64 y) does 
                return this;;;

        def int64 start() does
            X* x = new X(1,2);;
        """
        spp_tree = sppNewToS(sppClassesToS(sppTypes(addSppEndMethod(spplang.parse(program)))))
        s_tree   = functionCallLang.parse("(auto __ = &__memcpy(&__malloc(size of X), X{} as int8*, size of X) as X*).start(__,1,2)");

        NodeRenamer(lambda x: f"s{x[3:]}" if x.startswith("spplang_") else x).visit(spp_tree)
        self.assertEqual(Node2String().transform(s_tree), Node2String().transform(spp_tree.children[-1].children[-2].children[0].children[0].children[-1]))
        
    def test_simple_new2(self):
        program = """
        class X with 
            def X* start(X* this) does 
                return this;;;

        def int64 start() does
            X* x = new X();;
        """
        spp_tree = sppNewToS(sppClassesToS(sppTypes(addSppEndMethod(spplang.parse(program)))))
        s_tree   = functionCallLang.parse("(auto __ = &__memcpy(&__malloc(size of X), X{} as int8*, size of X) as X*).start(__)");

        NodeRenamer(lambda x: f"s{x[3:]}" if x.startswith("spplang_") else x).visit(spp_tree)
        self.assertEqual(Node2String().transform(s_tree), Node2String().transform(spp_tree.children[-1].children[-2].children[0].children[0].children[-1]))
 



     
if __name__ == "__main__":
    unittest.main()   
