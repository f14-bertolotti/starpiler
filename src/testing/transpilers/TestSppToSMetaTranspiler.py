import unittest

from src.testing.spplang import tests
from src.syntax.spplang import lang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers.spp.s import deltas
from src.transpilers.s import metric, metric01
from src.transpilers import MetaTranspiler

class Test(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            programString = Path(tests[f.__name__[5:]]["path"]).read_text()
            parsedTree = (lang.parse(programString))
            translatedTree = MetaTranspiler(deltas, metric01).search(parsedTree)
            self.assertEqual(run(program_tree=translatedTree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(Test, f"test_{testname}", make())
    

if __name__ == "__main__":
    unittest.main()

