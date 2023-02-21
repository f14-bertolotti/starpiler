import unittest

from src.testing.spplang import tests
from src.syntax.spplang import lang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers import deltas
from src.transpilers.s import metric01
from src.transpilers import MetaTranspiler
from src.utils import lang2rules
from src.syntax.slang import lang as slang

class Test(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            programString = Path(tests[f.__name__[5:]]["path"]).read_text()
            spp_tree = lang.parse(programString)
            s_tree = MetaTranspiler(deltas, None).search_Astar(spp_tree, lang2rules(slang))
            self.assertEqual(run(program_tree=s_tree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(Test, f"test_{testname}", make())
    

if __name__ == "__main__":
    unittest.main()

