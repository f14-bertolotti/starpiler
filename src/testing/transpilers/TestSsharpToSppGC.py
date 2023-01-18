import unittest

from src.syntax.slang import lang as slang
from src.syntax.spplang  import lang as spplang
from src.transpilers.spp import types as spptypes

from src.syntax.ssharplang  import lang as ssharplang
from src.transpilers.ssharp import types as ssharptypes
from src.transpilers.ssharp.spp import gc
from src.transpilers.ssharp.spp import classes
from src.transpilers.ssharp.spp import assignements
from src.transpilers.ssharp.spp import methods
from src.transpilers.ssharp.spp import identities
from src.transpilers.ssharp.spp import imports
from src.transpilers.ssharp.spp import fields
from src.transpilers.ssharp.spp import types as ssharp2spp_types

from src.transpilers.spp.s import transpile as spp2sTranspiler

from src.semantics.slang import run

from src.utils import SppPrettyPrinter
from src.utils import SPrettyPrinter

from lark.visitors import Transformer
class TypeIntoData(Transformer):
    def __default__(self, data, children, meta):
        data += f" {meta.type}"
        return super().__default__(data, children, meta)

class Test(unittest.TestCase):

    def test1(self):
        program = """
        from "src/testing/ssharplang/programs/simple_class.ss" import Simple as S ;
        class A {
            var int64 x;
            fun (A, int64 -> A) __init__(this, x) {
                this.x = x;
                return this;
            }
            fun ( -> int64) __main__ () {
                S s = new S(1);
                return 0;
            }
        }
        """
        sppgc = """from "src/testing/spplang/programs/gc/GC.spp" import GC as GC;"""
        sppgc = spptypes(spplang.parse(sppgc))
        parsed = ssharplang.parse(program)
        parsed = ssharptypes(parsed)
        parsed = ssharp2spp_types(parsed)
        parsed = gc(parsed)
        parsed = classes(parsed)
        parsed = fields(parsed)
        parsed = assignements(parsed)
        parsed = methods(parsed)
        parsed = imports(parsed)
        parsed = identities(parsed)

        self.assertEqual(sppgc.children[0].meta.type, parsed.children[0].meta.type)


        import rich
        rich.print("="*100)
        rich.print(program)
        rich.print("="*100)
        rich.print(SppPrettyPrinter().transform(parsed))
        rich.print("="*100)
        parsed = spp2sTranspiler(parsed)
        #rich.print(parsed)
        #rich.print("="*100)
        rich.print(SPrettyPrinter().transform(parsed))
        parsed = slang.parse(SPrettyPrinter().transform(parsed))
        #rich.print(slang.parse(SPrettyPrinter().transform(parsed)))

        run(program_tree=parsed)
        



if __name__ == "__main__":
    unittest.main()
