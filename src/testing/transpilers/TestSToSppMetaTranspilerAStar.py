import unittest

from src.testing.slang import tests
from src.semantics.slang import run
from pathlib import Path

from src.transpilers import deltas
from src.transpilers import MetaTranspiler
from src.transpilers import spp2s_transpile

from src.syntax import spplang
from src.syntax import slang

from src.utils import lang2rules

class Test(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            programString = Path(tests[f.__name__[5:]]["path"]).read_text()
            s_tree = slang.parse(programString)
            spp_tree = MetaTranspiler(deltas, None).search_Astar(s_tree, lang2rules(spplang))
            s_tree = spp2s_transpile(s_tree)
            self.assertEqual(run(program_tree=s_tree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    
    if testname not in {"point", "struct_class3", "struct_class2", "struct_class", "variable_declaration2", "sizeof_struct"}:

        setattr(Test, f"test_{testname}", make())
    

if __name__ == "__main__":
    unittest.main()

