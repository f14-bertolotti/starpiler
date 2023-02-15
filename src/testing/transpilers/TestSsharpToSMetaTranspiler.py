import unittest

from src.testing.ssharplang import tests
from src.syntax.ssharplang import lang
from src.semantics.slang import run
from pathlib import Path

from src.transpilers.ssharp.spp import deltas as ssharp2spp_deltas
from src.transpilers.spp.s import deltas as spp2s_deltas
from src.transpilers.s import metric01 as s_metric
from src.transpilers import MetaTranspiler

from src.transpilers.ssharp.spp import transpile as ssharp2spp_transpile
from src.transpilers.spp.s      import transpile as spp2s_transpile

from src.utils import NotAppliedException

def addname(f,start): 
    if isinstance(f, list): f = [addname(ff,start) for ff in f]
    else: f.__name__ = start + "_" + f.__name__
    return f

spp2s_deltas = [addname(d, "spp2s") for d in spp2s_deltas]
ssharp2spp_deltas = [addname(d, "ssharp2spp") for d in ssharp2spp_deltas]

class Test(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            code = Path(tests[f.__name__[5:]]["path"]).read_text()
            ssharp_tree = lang.parse(code)
            s_tree = MetaTranspiler(ssharp2spp_deltas + [spp2s_deltas], s_metric).search(ssharp_tree)
            self.assertEqual(run(program_tree=s_tree), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(Test, f"test_{testname}", make())
    

if __name__ == "__main__":
    unittest.main()

