import unittest

from src.syntax.spplang    import lang as spplang
from src.syntax.slang      import lang as slang

from src.transpilers.s.spp import structs
from src.transpilers.s.spp import identities
from src.transpilers.spp import isSpp
from src.utils import Node2String


class Test(unittest.TestCase):

    def test_simple_struct(self):
        program_s = """
        struct X with 
            X* x;
            int64 a = 1;
            int64 b = 2;
            int64 c;
        ;
        """
        program_spp = """
        class X with
            def X* x;
            def int64 a = 1;
            def int64 b = 2;
            def int64 c;
            def X* start(X* this) does return this;;
            def void end(X* this) does return;;
        ;
        """
        tree_s = structs(slang.parse(program_s))
        tree_spp = spplang.parse(program_spp)

        self.assertEqual(Node2String().transform(tree_s), Node2String().transform(tree_spp))
        self.assertTrue(isSpp(identities(tree_s)))

     
if __name__ == "__main__":
    unittest.main()   
