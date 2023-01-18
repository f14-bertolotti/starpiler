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

class Methods(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_method_definition(self, meta, nodes):
        self.applied = True

        plist = [x for c in zip(
            filter(lambda x:isinstance(x,Tree), nodes[1].children[0].children[1:]), 
            filter(lambda x:isinstance(x,Tree), nodes[3].children[1:-1])) for x in [Tree(Token("RULE", "spplang_parameter_definition"), list(c)), Token("COMMA",",")]]
        if len(plist) > 1: del plist[-1]

        res = Tree(Token('RULE', 'spplang_method_definition'), [
            Token('DEF', 'def'), 
            nodes[1].children[1].children[1], 
            nodes[2] if nodes[2].children[0].value != "__init__" else Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "start")]), 
            Tree(Token('RULE', 'spplang_parameter_seq_def'), [
                Token('LPAR', '('), 
                *plist,
                Token('RPAR', ')')]), 
            Token('DOES', 'does'), 
            nodes[5],
            Token('SEMICOLON',';')
            ], meta)
        return res


def methods(parseTree)->Tree:
    return Methods().transform(parseTree)
