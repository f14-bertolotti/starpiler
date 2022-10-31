
from lark.visitors import Transformer
from src.syntax.spplang import lang
from lark.tree import Tree
from lark import Token
from pathlib import Path

from src.transpilers.MetaTranspiler import MetaTranspiler
from src.transpilers import toString, isSLang

class SppToSImports(Transformer):
    def spplang_import(self, nodes):
        sppParseTree = lang.parse(Path(nodes[1].children[0].value[1:-1]).read_text())
        sParseTree = MetaTranspiler(SppToSImports.deltas, isSLang).search(sppParseTree)
        Path(nodes[1].children[0].value[1:-5]+".s").write_text(toString(sParseTree))
        return Tree(Token("RULE", "slang_import"), [
            Token("FROM", "from"), 
            Tree(Token("RULE", "slang_string"), [Token("__ANON__",nodes[1].children[0].value[:-5]+".s\"")]), 
            Token("IMPORT", "import"), 
            Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[3].children[0].value)]), 
            Token("AS", "as"), 
            Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[5].children[0].value)]), 
            Token("SEMICOLON", ";")])

def sppToSImports(parseTree): return SppToSImports().transform(parseTree)

from src.transpilers.RemoveSppClasses import removeSppClasses
from src.transpilers.SppToSIdentities import sppToSIdentities
SppToSImports.deltas = [removeSppClasses, sppToSIdentities, sppToSImports]

