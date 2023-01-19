from lark.visitors import Transformer
from src.utils     import NotAppliedException

class AppliedTransformer(Transformer):

    def __init__(self, *args, **kwargs):
        self.applied = False
        super().__init__(*args, **kwargs)

    def transform(self, *args, **kwargs):
        res = super().transform(*args, **kwargs)
        if not self.applied: raise NotAppliedException()
        return res



