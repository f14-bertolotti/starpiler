from lark.visitors import v_args
from lark.tree     import Tree
from lark          import Token

from src.utils import AppliedTransformer

class GlobalAssignements(AppliedTransformer):

    @v_args(meta=True)
    def slang_global_assignement(self, meta, nodes):
        self.applied = True
        return Tree(Token("RULE", "spplang_global_assignement"), [nodes[0]] + nodes[1].children, meta)

def globalAssignements(parseTree):
    return GlobalAssignements().transform(parseTree)
