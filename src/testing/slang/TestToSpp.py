from src.testing.slang     import tests
from src.transpilers.s.spp import transpile as SToSppTranspile
from src.transpilers.spp.s import transpile as SppToSTranspile
from src.syntax.slang      import lang
from src.semantics.slang   import run

from pathlib import Path
import unittest
import lark

class TestToSpp(unittest.TestCase):

    def test_point(self):
        programString = Path(tests["point"]["path"]).read_text()
        SParseTree = lang.parse(programString)
        with self.assertRaises(lark.exceptions.VisitError):
            SToSppTranspile(SParseTree)
        
    def test_struct_class3(self):
        programString = Path(tests["struct_class3"]["path"]).read_text()
        SParseTree = lang.parse(programString)
        with self.assertRaises(lark.exceptions.VisitError):
            SToSppTranspile(SParseTree)
        
    def test_struct_class2(self):
        programString = Path(tests["struct_class2"]["path"]).read_text()
        SParseTree = lang.parse(programString)
        with self.assertRaises(lark.exceptions.VisitError):
            SToSppTranspile(SParseTree)
 
    def test_struct_class(self):
        programString = Path(tests["struct_class"]["path"]).read_text()
        SParseTree = lang.parse(programString)
        with self.assertRaises(lark.exceptions.VisitError):
            SToSppTranspile(SParseTree)
 
    def test_sizeof_struct(self):
        programString = Path(tests["struct_class"]["path"]).read_text()
        SParseTree = lang.parse(programString)
        with self.assertRaises(lark.exceptions.VisitError):
            SToSppTranspile(SParseTree)
 
for testname in tests:
    def make():
        def f(self):
            programString = Path(tests[f.__name__[5:]]["path"]).read_text()
            SparseTree    = lang.parse(programString)
            SppParseTree  = SToSppTranspile(SparseTree)
            SparseTree    = SppToSTranspile(SppParseTree)
            #import rich
            #rich.print(SppParseTree)
            #rich.print(programString)

            self.assertEqual(run(program_tree=SparseTree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    if testname not in {"point", "struct_class3", "struct_class2", "struct_class", "sizeof_struct"}:
        setattr(TestToSpp, f"test_{testname}", make())

if __name__ == "__main__":
    unittest.main()

