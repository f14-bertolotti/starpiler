import unittest
from src.testing.ssharplang import tests
from src.semantics.slang import run
from pathlib import Path

from src.syntax import ssharplang

from src.transpilers import deltas 
from src.transpilers.spp import metric01 as sppmetric
from src.transpilers import MetaTranspiler

from src.transpilers.spp.s      import transpile as spp2s_transpile


class Test(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            code = Path(tests[f.__name__[5:]]["path"]).read_text()
            ssharp_tree = ssharplang.parse(code)
            spp_tree = MetaTranspiler(deltas, sppmetric).search(ssharp_tree)
            s_tree = spp2s_transpile(spp_tree)
            self.assertEqual(run(program_tree=s_tree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(Test, f"test_{testname}", make())
    

if __name__ == "__main__":
    unittest.main()

