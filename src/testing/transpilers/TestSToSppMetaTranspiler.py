import unittest

from src.testing.slang import tests
from src.syntax.slang import lang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers import deltas
from src.transpilers.spp import metric01
from src.transpilers import MetaTranspiler
from src.transpilers.spp.s import transpile

class Test(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            programString = Path(tests[f.__name__[5:]]["path"]).read_text()
            parsedTree = lang.parse(programString)
            translatedTree = MetaTranspiler(deltas, metric01).search(parsedTree)
            SParseTree = transpile(translatedTree)
            self.assertEqual(run(program_tree=SParseTree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    
    if testname not in {"point", "struct_class3", "struct_class2", "struct_class", "sizeof_struct"}:
        setattr(Test, f"test_{testname}", make())
    

if __name__ == "__main__":
    unittest.main()

