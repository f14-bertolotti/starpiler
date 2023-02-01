from lark.visitors import Transformer
from lark import Tree, Token
from src.transpilers.ssharp.spp.Utils import gcPop, gcEnd
import copy

class FuturePopsSsharp(Transformer):

    def ssharplang_pop_block(self, nodes):

        if isinstance(nodes[-2], Tree) and nodes[-2].data in {"ssharplang_return","ssharplang_return_void"}:
            if gcEnd in nodes:
                for _ in range(nodes[-1]): nodes.insert(nodes.index(gcEnd), copy.deepcopy(gcPop))
            else:
                for _ in range(nodes[-1]): nodes.insert(-2, copy.deepcopy(gcPop))

        return Tree(Token("RULE","ssharplang_block"), nodes[:-1])

futurePopsSsharp = FuturePopsSsharp()
def futurepops_ssharp(parseTree):
    return futurePopsSsharp.transform(parseTree)
