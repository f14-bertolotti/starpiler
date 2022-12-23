
from lark.visitors import v_args, Transformer
from src.syntax.slang import lang
from lark.tree import Tree
from lark import Token
from pathlib import Path

from src.transpilers.s.spp import structs
from src.transpilers.s.spp import identities

from src.utils import SppPrettyPrinter
import tempfile


class Imports(Transformer):
    path2cached = dict()
    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)

    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise ValueError("Not applied")
        return res

    @v_args(meta=True)
    def slang_import(self, meta, nodes):
        importpath = Path(nodes[1].children[0].value[1:-1])
        
        if importpath not in Imports.path2cached:
            Imports.path2cached[importpath] = tempfile.NamedTemporaryFile()

            parseTree = lang.parse(importpath.read_text())
            for fun in [structs, Imports().transform, identities]:
                try:
                    parseTree = fun(parseTree)
                except ValueError as e: continue
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



#    @v_args(tree=True)
#    def slang_import(self, tree):
#
#        sParseTree = cachedPaths[importpath] if importpath in cachedPaths else lang.parse(Path(importpath).read_text())
#        if importpath not in cachedPaths: cachedPaths[importpath] = sParseTree
#
#        path = Path(nodes[1].children[0].value[1:-5].replace("/",".")+".s")
#        
#        if not path.exists(): 
#            sppParseTree = identities(structs(Imports().transform(sppParseTree)))
#            path.write_text(SPrettyPrinter().transform(sParseTree))
#
#        self.applied = True
#        return Tree(Token("RULE", "spplang_import"), [
#                   Token("FROM", "from"), 
#                   Tree(Token("RULE", "spplang_string"), [Token("__ANON__",nodes[1].children[0].value[:-5]+".s\"")]), 
#                   Token("IMPORT", "import"), 
#                   Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", nodes[3].children[0].value)]), 
#                   Token("AS", "as"), 
#                   Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", nodes[5].children[0].value)]), 
#                   Token("SEMICOLON", ";")], meta)

def imports(parseTree): 
    return Imports().transform(parseTree)





