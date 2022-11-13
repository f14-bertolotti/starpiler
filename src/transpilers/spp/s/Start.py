
from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Token
import copy
class Start(Transformer):

    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)
    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise ValueError("Not applied")
        return res


    @v_args(meta=True)
    def spplang_start(self, meta, nodes):
        self.applied = True
        return Tree(Token("RULE","slang_start"), nodes, copy.deepcopy(meta))

def start(parseTree):
    return Start().transform(parseTree)

