from lark.visitors import v_args
from lark import Tree, Token
from src.semantics.types import * 

from src.utils import AppliedTransformer

class ClassAccesses(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_class_access(self, meta, nodes):
        self.applied = True
        return Tree(Token('RULE', 'spplang_struct_access'), nodes) 


def classAccesses(parseTree)->Tree:
    return ClassAccesses().transform(parseTree)
