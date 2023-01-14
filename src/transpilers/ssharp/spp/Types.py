from lark.visitors import v_args
from lark.tree import Tree
from lark import Token
from src.semantics.types import * 

from src.utils import AppliedTransformer

def objectToPointerType(t, v):
    if isinstance(t, Object):
        t.base = objectToPointerType(t.base, v)
        t = Pointer(t.base)
    elif isinstance(t, Pointer):
        t.base = objectToPointerType(t.base, v)
    elif isinstance(t, Array):
        t.base = objectToPointerType(t.base, v)
    elif isinstance(t, FType):
        t.ptypes = [objectToPointerType(p, v) for p in t.ptypes]
        t.rtype = objectToPointerType(t.rtype, v)
    elif isinstance(t, SType):
        if t not in v:
            v.append(t)
            t.name2type = {n:objectToPointerType(t,v+[t]) for n,t in t.name2type.items()}
    return t

class Types(AppliedTransformer):

    def __default__(self, data, nodes, meta):
        self.applied = True
        meta.type = objectToPointerType(meta.type, [])
        return super().__default__(data, nodes, meta) 

def types(parseTree)->Tree:
    return Types().transform(parseTree)
