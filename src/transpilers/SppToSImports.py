
from lark.visitors import Transformer, Visitor
from src.syntax.spplang import lang
from lark.tree import Tree
from lark import Token
from pathlib import Path

from src.transpilers.MetaTranspiler import MetaTranspiler
from src.transpilers import toString, isSLang

class SppToSImports(Transformer):
    def spplang_import(self, nodes):
        sppParseTree = lang.parse(Path(nodes[1].children[0].value[1:-1]).read_text())
        if not (path := Path(nodes[1].children[0].value[1:-5]+".s")).exists(): 
            sParseTree = MetaTranspiler(SppToSImports.deltas, isSLang).search(sppParseTree)
            path.write_text(toString(sParseTree))

        class GetImported(Visitor):
            def __init__(self, name, *args, **kwargs):
                self.name, self.result = name, None
                super().__init__(*args, **kwargs)
            def visit(self, *args, **kwargs):
                if self.result == None: raise ValueError(f"SppToSImport error, name \"{self.name}\" not found")
                return self.result
            def spplang_function_definition(self, tree):
                if tree.children[2].children[0] == self.name: self.result = tree
            def spplang_function_declaration(self, tree):
                if tree.children[2].children[0] == self.name: self.result = tree
            def spplang_global_assignement(self, tree):
                if tree.children[2].children[0] == self.name: self.result = tree
            def spplang_class(self, tree):
                if tree.children[1].children[0] == self.name: self.result = tree

        class AddImported(Transformer):
            def __default__(self, data, children, meta):
                return Tree(f"imported_{data}", children, meta)

        return Tree(Token("RULE", "spplang_imported"), [
                   Tree(Token("RULE", "slang_import"), [
                       Token("FROM", "from"), 
                       Tree(Token("RULE", "slang_string"), [Token("__ANON__",nodes[1].children[0].value[:-5]+".s\"")]), 
                       Token("IMPORT", "import"), 
                       Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[3].children[0].value)]), 
                       Token("AS", "as"), 
                       Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", nodes[5].children[0].value)]), 
                       Token("SEMICOLON", ";")]), 
                   AddImported().transform(GetImported(nodes[3].children[0]).visit(sppParseTree))])

def sppToSImports(parseTree): return SppToSImports().transform(parseTree)

from src.transpilers.SppClassesToSStruct import sppClassesToSStruct
from src.transpilers.SppToSIdentities import sppToSIdentities
SppToSImports.deltas = [sppClassesToSStruct, sppToSIdentities, sppToSImports]

