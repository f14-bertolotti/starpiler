from lark.visitors import v_args
from lark.tree import Tree
from lark import Token
from pathlib import Path

from src.transpilers.ssharp     import types
from src.transpilers.ssharp.spp import gc4imports
from src.transpilers.ssharp.spp import types as ssharp2spp_types
from src.transpilers.ssharp.spp import methods
from src.transpilers.ssharp.spp import arrays
from src.transpilers.ssharp.spp import newofs, news
from src.transpilers.ssharp.spp import classes
from src.transpilers.ssharp.spp import assignements
from src.transpilers.ssharp.spp import fields
from src.transpilers.ssharp.spp import identities
from src.syntax.ssharplang      import lang

from src.utils import AppliedTransformer
from src.utils import SppPrettyPrinter
from src.utils import AppliedTransformer
from src.utils import NotAppliedException

import tempfile


class Imports(AppliedTransformer):
    path2cached = dict()

    @v_args(meta=True)
    def ssharplang_import(self, meta, nodes):
        importpath = Path(nodes[1].children[0].value[1:-1])
        
        if importpath not in Imports.path2cached:
            Imports.path2cached[importpath] = tempfile.NamedTemporaryFile()

            parseTree = lang.parse(importpath.read_text())
            for delta in [types, ssharp2spp_types, gc4imports, classes, fields, methods, arrays, news, newofs, assignements, Imports().transform, identities]:
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


