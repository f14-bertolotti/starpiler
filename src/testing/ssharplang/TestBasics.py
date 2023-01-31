import unittest

from src.syntax.slang import lang as slang
from src.syntax.spplang  import lang as spplang
from src.transpilers.spp import types as spptypes

from src.syntax.ssharplang  import lang as ssharplang
from src.transpilers.ssharp import types as ssharptypes

from src.transpilers.spp.s import transpile as spp2sTranspiler
from src.transpilers.ssharp.spp import transpile as ssharp2sppTranspiler

from src.semantics.slang import run

from src.utils import SppPrettyPrinter
from src.utils import SPrettyPrinter

from lark.visitors import Transformer
from pathlib import Path
import rich

class Test(unittest.TestCase):

    def test1(self):
        program = """
        from "src/testing/ssharplang/programs/simple_class.ss" import Simple as S ;
        class A {
            var int64 x;
            fun (A, int64 -> A) __init__(this, x) {
                this.x = x;
                return this;
            }
            fun ( -> int64) __main__ () {
                S s = new S(1);
                return s.x;
            }
        }
        """
        sppgc = """from "src/testing/spplang/programs/gc/GC.spp" import GC as GC;"""
        sppgc = spptypes(spplang.parse(sppgc))
        sharp_parsed = ssharplang.parse(program)
        spp_parsed = ssharp2sppTranspiler(sharp_parsed)
        s_parsed = spp2sTranspiler(spp_parsed)
        self.assertEqual(run(program_tree=s_parsed), 1)
        
    def test_integer_array(self):
        program = Path("src/testing/ssharplang/programs/IntegerArray.ss").read_text()
        ssharp_parsed = ssharplang.parse(program)
        spp_parsed = ssharp2sppTranspiler(ssharp_parsed)
        s_parsed = spp2sTranspiler(spp_parsed)
        self.assertEqual(run(program_tree=s_parsed),1)


    def test_array(self):
        program = Path("src/testing/ssharplang/programs/IntArray.ss").read_text()
        ssharp_parsed = ssharplang.parse(program)
        spp_parsed = ssharp2sppTranspiler(ssharp_parsed)
        s_parsed = spp2sTranspiler(spp_parsed)
        self.assertEqual(run(program_tree=s_parsed),1)

    def test_matrix(self):
        program = Path("src/testing/ssharplang/programs/IntMatrix.ss").read_text()
        ssharp_parsed = ssharplang.parse(program)
        spp_parsed = ssharp2sppTranspiler(ssharp_parsed)
        s_parsed = spp2sTranspiler(spp_parsed)
        self.assertEqual(run(program_tree=s_parsed),1)





if __name__ == "__main__":
    unittest.main()
