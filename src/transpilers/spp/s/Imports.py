
from lark.visitors      import v_args
from src.syntax.spplang import lang
from lark.tree          import Tree
from lark               import Token
from pathlib            import Path

from src.transpilers.spp   import addEndMethods
from src.transpilers.spp   import types
from src.transpilers.spp.s import classes
from src.transpilers.spp.s import news
from src.transpilers.spp.s import classAccesses
from src.transpilers.spp.s import identities

from src.utils import SPrettyPrinter
from src.utils import AppliedTransformer
from src.utils import NotAppliedException

import tempfile


class Imports(AppliedTransformer):
    path2cached = dict()

    @v_args(meta=True)
    def spplang_import(self, meta, nodes):
        importpath = Path(nodes[1].children[0].value[1:-1])
        
        if importpath not in Imports.path2cached:
            Imports.path2cached[importpath] = tempfile.NamedTemporaryFile()

            parseTree = lang.parse(importpath.read_text())
            for delta in [types, addEndMethods, Imports().transform, classes, news, classAccesses, identities]:
                try: parseTree = delta(parseTree)
                except NotAppliedException: continue
            Imports.path2cached[importpath].write(SPrettyPrinter().transform(parseTree).encode("utf-8"))
            Imports.path2cached[importpath].flush()

        self.applied = True
        return Tree(Token("RULE", "slang_import"), [
                   Token("FROM", "from"), 
                   Tree(Token("RULE", "slang_string"), [Token("__ANON__", f"\"{self.path2cached[importpath].name}\"")]), 
                   Token("IMPORT", "import"), 
                   Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[3].children[0].value)]), 
                   Token("AS", "as"), 
                   Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[5].children[0].value)]), 
                   Token("SEMICOLON", ";")], meta)


def imports(parseTree): 
    return Imports().transform(parseTree)


