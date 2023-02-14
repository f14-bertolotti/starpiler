import unittest

from src.testing.ssharplang import tests
from src.syntax.ssharplang import lang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers.spp.s import transpile as spp2s_transpile
from src.transpilers.ssharp.spp import transpile as ssharp2spp_transpile

class TestBasics(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            code        = Path(tests[f.__name__[5:]]["path"]).read_text()
            ssharp_tree = lang.parse(code)
            spp_tree    = ssharp2spp_transpile(ssharp_tree)
            s_tree      = spp2s_transpile(spp_tree)
            self.assertEqual(run(program_tree=s_tree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(TestBasics, f"test_{testname}", make())

if __name__ == "__main__":
    unittest.main()

