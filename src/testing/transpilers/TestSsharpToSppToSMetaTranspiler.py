import unittest

from src.testing.ssharplang import tests
from src.semantics.slang import run
from pathlib import Path

from src.syntax import ssharplang

from src.transpilers import MetaTranspiler
from src.transpilers import ssharp2spp_deltas
from src.transpilers import spp2s_deltas
from src.transpilers.spp import metric01 as spp_metric
from src.transpilers.s   import metric01 as s_metric


class Test(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            code = Path(tests[f.__name__[5:]]["path"]).read_text()
            ssharp_tree = ssharplang.parse(code)
            spp_tree = MetaTranspiler(ssharp2spp_deltas, spp_metric).search(ssharp_tree)
            s_tree   = MetaTranspiler(spp2s_deltas, s_metric).search(spp_tree   )
            self.assertEqual(run(program_tree=s_tree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(Test, f"test_{testname}", make())
    

if __name__ == "__main__":
    unittest.main()

