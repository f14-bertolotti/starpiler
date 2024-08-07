from lark.visitors import Transformer
from lark          import Token
from lark.tree     import Tree

class Node2String(Transformer):
        
    def __default__(self, data, children, meta):
        result = super().__default__(data, children, meta)
        result.string = " ".join([child.value if isinstance(child, Token) else child.string for child in children]) 
        return result
        
    def transform(self, *args, **kwargs):
        return super().transform(*args, **kwargs).string

