import unittest

from src.testing.spplang import tests
from src.syntax.spplang import lang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers.spp.s import transpile

class TestBasics(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            code = Path(tests[f.__name__[5:]]["path"]).read_text()
            parsedTree = lang.parse(code)
            transpiledTree = transpile(parsedTree)
            self.assertEqual(run(program_tree=transpiledTree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(TestBasics, f"test_{testname}", make())

if __name__ == "__main__":
    unittest.main()

