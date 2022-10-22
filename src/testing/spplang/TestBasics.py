import unittest

from src.testing.spplang import tests
from src.syntax.spplang import lang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers import MetaTranspiler, isSLang, deltas

class TestBasics(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            parsedTree = MetaTranspiler(deltas, isSLang).search(lang.parse(Path(tests[f.__name__[5:]]["path"]).read_text()))
            self.assertEqual(run(program_tree=parsedTree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(TestBasics, f"test_{testname}", make())

if __name__ == "__main__":
    unittest.main()

