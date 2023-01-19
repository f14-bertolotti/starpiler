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

        parsed = ssharp2sppTranspiler(ssharplang.parse(program))
        self.assertEqual(sppgc.children[0].meta.type, parsed.children[0].meta.type)
        parsed = spp2sTranspiler(parsed)
        self.assertEqual(run(program_tree=parsed), 1)
        
    def test_array(self):
        program = Path("src/testing/ssharplang/programs/IntArray.ss").read_text()

        import rich

        ssharp_parsed = ssharplang.parse(program)

        rich.print(program)
        rich.print("="*100)

        spp_parsed    = ssharp2sppTranspiler(ssharp_parsed)

        rich.print(SppPrettyPrinter().transform(spp_parsed))
        rich.print("="*100)

        s_parsed      = spp2sTranspiler(spp_parsed)

        rich.print(SPrettyPrinter().transform(s_parsed))

        run(program_tree=s_parsed)



if __name__ == "__main__":
    unittest.main()
