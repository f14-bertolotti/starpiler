
from lark.visitors import Transformer, Visitor
from src.syntax.spplang import lang
from lark.tree import Tree
from lark import Token
from pathlib import Path

from src.transpilers.AddSppEndMethod    import addSppEndMethod
from src.transpilers.SppTypes           import sppTypes
from src.transpilers.SppClassesToS      import sppClassesToS
from src.transpilers.SppNewToS          import sppNewToS
from src.transpilers.SppStructAccessToS import sppStructAccessToS
from src.transpilers.SppToSIdentities   import sppToSIdentities
from src.utils import SPrettyPrinter


class SppToSImport(Transformer):
    def spplang_import(self, nodes):
        sppParseTree = lang.parse(Path(nodes[1].children[0].value[1:-1]).read_text())
        path = Path(nodes[1].children[0].value[1:-5]+".s")
        if not path.exists(): 
            sParseTree = sppToSIdentities(sppStructAccessToS(sppNewToS(sppClassesToS(addSppEndMethod(sppTypes(sppParseTree))))))
            path.write_text(SPrettyPrinter().transform(sParseTree))

        return Tree(Token("RULE", "slang_import"), [
                   Token("FROM", "from"), 
                   Tree(Token("RULE", "slang_string"), [Token("__ANON__",nodes[1].children[0].value[:-5]+".s\"")]), 
                   Token("IMPORT", "import"), 
                   Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[3].children[0].value)]), 
                   Token("AS", "as"), 
                   Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[5].children[0].value)]), 
                   Token("SEMICOLON", ";")])

def sppToSImport(parseTree): 
    return SppToSImport().transform(parseTree)


