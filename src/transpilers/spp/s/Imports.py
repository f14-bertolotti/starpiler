
from lark.visitors import Transformer
from src.syntax.spplang import lang
from lark.tree import Tree
from lark import Token
from pathlib import Path

from src.transpilers.spp   import addEndMethods
from src.transpilers.spp   import types
from src.transpilers.spp.s import classes
from src.transpilers.spp.s import news
from src.transpilers.spp.s import classAccesses
from src.transpilers.spp.s import identities
from src.utils import SPrettyPrinter

cachedPaths = dict()
class Imports(Transformer):

    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)
    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise ValueError("Not applied")
        return res


    def spplang_import(self, nodes):
        importpath = nodes[1].children[0].value[1:-1] 
        sppParseTree = cachedPaths[importpath] if importpath in cachedPaths else lang.parse(Path(importpath).read_text())
        if importpath not in cachedPaths: cachedPaths[importpath] = sppParseTree

        path = Path(nodes[1].children[0].value[1:-5]+".s")
        if not path.exists(): 
            sParseTree = identities(classAccesses(news(classes(Imports().transform(addEndMethods(types(sppParseTree)))))))
            path.write_text(SPrettyPrinter().transform(sParseTree))

        self.applied = True
        return Tree(Token("RULE", "slang_import"), [
                   Token("FROM", "from"), 
                   Tree(Token("RULE", "slang_string"), [Token("__ANON__",nodes[1].children[0].value[:-5]+".s\"")]), 
                   Token("IMPORT", "import"), 
                   Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[3].children[0].value)]), 
                   Token("AS", "as"), 
                   Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[5].children[0].value)]), 
                   Token("SEMICOLON", ";")])

def imports(parseTree): 
    return Imports().transform(parseTree)


