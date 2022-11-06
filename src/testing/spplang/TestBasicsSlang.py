import unittest

from src.testing.slang import tests
from src.syntax.slang import lang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers import MetaTranspiler, isSLang, isSppLang, deltas

class TestBasicsSlang(unittest.TestCase): pass

for testname in filter(lambda x:x not in {"point", "struct_class", "struct_class2", "struct_class3"}, tests):
    def make():
        def f(self):
            parsedTree = MetaTranspiler(deltas, isSLang).search(MetaTranspiler(deltas, isSppLang).search(lang.parse(Path(tests[f.__name__[5:]]["path"]).read_text())))
            self.assertEqual(run(program_tree=parsedTree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(TestBasicsSlang, f"test_{testname}", make())

if __name__ == "__main__":
    unittest.main()

