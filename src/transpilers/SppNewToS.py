from lark.visitors import Transformer, Visitor
from lark.tree import Tree
from lark import Token
from src.transpilers import toString
from src.transpilers import addBeforeReturn
from pathlib import Path

from src.transpilers import isSppLang


class SppNewToS(Transformer)

    def __init__(self, *args, **kwargs):
        self.name2class = dict()
        super().__init__(*args, *kwargs)

    def spplang_import(self, nodes):
        raise ValueError("spplang_import should be removed")
    
    def slang_import(self, nodes):
        self.ugen.program += Path(nodes[1].children[0].value[1:-1]).read_text()
        return Tree(Token("RULE", "slang_import"), nodes)

    def spplang_new(self, nodes):
        raise NotImplemented("spplang_new")

    def spplang_function_call(self, nodes):
        raise NotImplemented("spplang_function_call")



def sppNewToS(parseTree):
    return SppNewToS().transform(parseTree)

