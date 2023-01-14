from lark.visitors import Transformer
from lark.tree import Tree
from lark import Token

class TreeAnon(Transformer):

    def __default__(self, data, children, meta):
        for child in children:
            if isinstance(child, Token) and child.type.startswith("__ANON_"):
                child.type = "__ANON__"
        return Tree(data, children, meta)
