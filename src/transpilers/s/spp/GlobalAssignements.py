from lark.visitors import v_args, Transformer
from lark.tree import Tree
from lark import Token

class GlobalAssignements(Transformer):

    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)

    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise ValueError("Not applied")
        return res

    @v_args(meta=True)
    def slang_global_assignement(self, meta, nodes):
        self.applied = True
        return Tree(Token("RULE", "spplang_global_assignement"), [nodes[0]] + nodes[1].children, meta)

def globalAssignements(parseTree):
    return GlobalAssignements().transform(parseTree)
