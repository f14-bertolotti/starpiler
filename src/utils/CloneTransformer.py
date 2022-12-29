from lark.visitors import Transformer
from lark.tree import Tree

class CloneTransformer(Transformer):
    def __default__(self, data, children, meta):
        return Tree(data, children, meta)


