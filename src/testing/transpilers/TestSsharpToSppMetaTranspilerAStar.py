import unittest

from src.testing.ssharplang import tests
from src.syntax.ssharplang import lang
from src.syntax.spplang import lang as spplang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers.ssharp.spp import deltas as ssharp2spp_deltas
from src.transpilers.spp import metric01 as sppmetric
from src.transpilers import MetaTranspiler

from src.transpilers.ssharp.spp import transpile as ssharp2spp_transpile
from src.transpilers.spp.s      import transpile as spp2s_transpile

from src.utils import lang2rules

class Test(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            code = Path(tests[f.__name__[5:]]["path"]).read_text()
            ssharp_tree = lang.parse(code)
            spp_tree = MetaTranspiler(ssharp2spp_deltas, sppmetric).search_Astar(ssharp_tree, lang2rules(spplang))

            #import rich
            #rich.print(spp_tree)

            #from src.utils import SppPrettyPrinter
            #print(SppPrettyPrinter().transform(spp_tree))
            #rich.print(spplang.parse(SppPrettyPrinter().transform(spp_tree)))

            s_tree = spp2s_transpile(spp_tree)
            self.assertEqual(run(program_tree=s_tree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(Test, f"test_{testname}", make())
    

if __name__ == "__main__":
    unittest.main()

