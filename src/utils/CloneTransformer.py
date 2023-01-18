from lark.visitors import Transformer
from lark.tree import Tree

class CloneTransformer(Transformer):
    
    def __init__(self, notypes=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.notypes = notypes

    def __default__(self, data, children, meta):
        if self.notypes: meta.type = None
        return Tree(data, children, meta)


