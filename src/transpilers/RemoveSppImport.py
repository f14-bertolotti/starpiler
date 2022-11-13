
from lark.visitors import Visitor, Transformer
from src.syntax.spplang import lang
from lark.tree import Tree
from lark import Token
from pathlib import Path

from src.transpilers.MetaTranspiler import MetaTranspiler
from src.transpilers import toString, isSLang

class RemoveSppImports(Transformer):
    def __init__(self, *args, **kwargs):
        self.spplang_start_run = False
        super().__init__(*args, **kwargs)

    def transform(self, *args, **kwargs):
        result = super().transform(*args, **kwargs)
        if not self.spplang_start_run: raise ValueError("import could generate the new branch")
        return result

    def spplang_import(self, nodes):
        sppParseTree = lang.parse(Path(nodes[1].children[0].value[1:-1]).read_text())
        oldname, newname = nodes[3].children[0].value, nodes[5].children[0].value

        # TODO rename only last usages
        # because malloc extern and class malloc can could coexists.
        class Rename(Transformer):
            def __init__(self, oldname, newname, *args, **kwargs):
                self.oldname, self.newname = oldname, newname
                super().__init__(*args, **kwargs)
            def spplang_identifier(self, nodes):
                return Tree(Token("RULE","spplang_identifier"), [Token("__ANON__", self.newname if nodes[0] == self.oldname else nodes[0].value)])
                
        return Rename(oldname, newname).transform(sppParseTree).children

    def spplang_start(self, nodes):
        self.spplang_start_run = True
        return Tree(Token("RULE", "spplang_start"), [sub for node in nodes for sub in (node if isinstance(node,list) else [node])])
            
                
def removeSppImports(parseTree): 
    return RemoveSppImports().transform(parseTree)
