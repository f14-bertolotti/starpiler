from lark.visitors import Transformer
from lark.tree import Tree
from lark import Token


class AddBeforeReturn(Transformer):

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree
        super().__init__(*args, **kwargs)

    def __default__(self, data, children, meta):
        return super().__default__(data, [sub for child in children for sub in (child if isinstance(child,list) else [child])], meta)

    def slang_return_void(self, nodes):
        return [self.tree, Tree(Token("RULE", "slang_return_void"), nodes)]


def addBeforeReturn(addedTree, otherTree):
    return AddBeforeReturn(addedTree).transform(otherTree)
