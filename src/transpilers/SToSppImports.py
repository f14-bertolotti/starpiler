
from lark.visitors import Transformer
from src.syntax.slang import lang
from lark.tree import Tree
from lark import Token
from pathlib import Path

from src.transpilers.MetaTranspiler import MetaTranspiler
from src.transpilers import toString, isSppLang

class SToSppImports(Transformer):
    def slang_import(self, nodes):
        sParseTree = lang.parse(Path(nodes[1].children[0].value[1:-1]).read_text())
        if not (path := Path(nodes[1].children[0].value[1:-3]+".spp")).exists(): 
            sppParseTree = MetaTranspiler(SToSppImports.deltas, isSppLang).search(sParseTree)
            path.write_text(toString(sppParseTree))
        return Tree(Token("RULE", "spplang_import"), [
            Token("FROM", "from"), 
            Tree(Token("RULE", "spplang_string"), [Token("__ANON__",nodes[1].children[0].value[:-3]+".spp\"")]), 
            Token("IMPORT", "import"), 
            Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", nodes[3].children[0].value)]), 
            Token("AS", "as"), 
            Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", nodes[5].children[0].value)]), 
            Token("SEMICOLON", ";")])

def sToSppImports(parseTree): return SToSppImports().transform(parseTree)

from src.transpilers.SToSppIdentities import sToSppIdentities
from src.transpilers.SStructToSppClass import sStructToSppClass 
SToSppImports.deltas = [sToSppIdentities, sStructToSppClass, sToSppImports]

