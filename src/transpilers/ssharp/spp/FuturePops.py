from lark import Tree, Token
from src.transpilers.ssharp.spp.Utils import gcPop, gcEnd
from src.utils import AppliedTransformer
import copy

class FuturePopsSsharp(AppliedTransformer):

    def reset(self):
        self.applied = False
        return self

    def ssharplang_pop_block(self, nodes):
        self.applied = True

        if isinstance(nodes[-2], Tree) and nodes[-2].data in {"ssharplang_return","ssharplang_return_void"}:
            if gcEnd in nodes:
                for _ in range(nodes[-1]): nodes.insert(nodes.index(gcEnd), copy.deepcopy(gcPop))
            else:
                for _ in range(nodes[-1]): nodes.insert(-2, copy.deepcopy(gcPop))

        return Tree(Token("RULE","ssharplang_block"), nodes[:-1])

transformer = FuturePopsSsharp()
def futurepops_ssharp(parseTree):
    return transformer.reset().transform(parseTree)
