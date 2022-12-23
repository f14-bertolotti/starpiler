from src.testing.slang     import tests
from src.transpilers.s.spp import transpile as SToSppTranspile
from src.transpilers.spp.s import transpile as SppToSTranspile
from src.syntax.slang      import lang
from src.semantics.slang   import run

from pathlib import Path
import unittest
import rich

class TestToSpp(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            print()
            programString = Path(tests[f.__name__[5:]]["path"]).read_text()
            rich.print(programString)
            print("="*35)
            SparseTree    = lang.parse(programString)
            rich.print(SparseTree)
            print("="*35)
            SppParseTree  = SToSppTranspile(SparseTree)
            rich.print(SppParseTree)
            print("="*35)
            SparseTree    = SppToSTranspile(SppParseTree)
            rich.print(SparseTree)
            print("="*35)


            self.assertEqual(run(program_tree=SparseTree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(TestToSpp, f"test_{testname}", make())

if __name__ == "__main__":
    unittest.main()

