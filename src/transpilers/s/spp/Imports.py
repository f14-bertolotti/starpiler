
from lark.visitors    import v_args
from src.syntax.slang import lang
from lark.tree        import Tree
from lark             import Token
from pathlib          import Path

from src.transpilers.s.spp import structs
from src.transpilers.s.spp import identities

from src.utils import AppliedTransformer
from src.utils import NotAppliedException
from src.utils import SppPrettyPrinter

import tempfile, lark

class Imports(AppliedTransformer):
    path2cached = dict()

    def transform(self, *args, **kwargs):
        try:
            res = super().transform(*args, **kwargs)
            return res
        except lark.exceptions.VisitError: raise NotAppliedException

    @v_args(meta=True)
    def slang_import(self, meta, nodes):
        importpath = Path(nodes[1].children[0].value[1:-1])
        
        if importpath not in Imports.path2cached:
            Imports.path2cached[importpath] = tempfile.NamedTemporaryFile()

            parseTree = lang.parse(importpath.read_text())
            for delta in [structs, Imports().transform, identities]:
                try: parseTree = delta(parseTree)
                except NotAppliedException: continue

            Imports.path2cached[importpath].write(SppPrettyPrinter().transform(parseTree).encode("utf-8"))
            Imports.path2cached[importpath].flush()

        self.applied = True
        return Tree(Token("RULE", "spplang_import"), [
                   Token("FROM", "from"), 
                   Tree(Token("RULE", "spplang_string"), [Token("__ANON__", f"\"{self.path2cached[importpath].name}\"")]), 
                   Token("IMPORT", "import"), 
                   Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", nodes[3].children[0].value)]), 
                   Token("AS", "as"), 
                   Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", nodes[5].children[0].value)]), 
                   Token("SEMICOLON", ";")], meta)

def imports(parseTree): 
    return Imports().transform(parseTree)

