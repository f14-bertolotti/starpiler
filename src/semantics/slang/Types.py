from abc import abstractmethod
from llvmlite.ir import VoidType, IntType, DoubleType, PointerType, FunctionType


class Type: 
    abstractmethod
    def toLLVM(self): pass
    abstractmethod
    def __len__(self): pass
    def __eq__(self, other): return str(self) == str(other) 
    def __neq__(self, other):return str(self) != str(other)
    def __hash__(self): return hash(self.__class__)
class Void(Type):
    def toLLVM(self): return VoidType()
    def __str__(self): return "Void"
    def __len__(self): raise ValueError("Void Type has no size")
class Int8(Type): 
    def toLLVM(self): return IntType(8)
    def __str__(self): return "Int8"
    def __len__(self): return 1
class Int32(Type):
    def toLLVM(self): return IntType(32)
    def __str__(self): return "Int32"
    def __len__(self): return 2
class Int64(Type): 
    def toLLVM(self): return IntType(64)
    def __str__(self): return "Int64"  
    def __len__(self): return 4
class Double(Type): 
    def toLLVM(self): return DoubleType()
    def __str__(self): return "Double"
    def __len__(self): return 8
class Pointer(Type):
    def __init__(self, base): self.base = base
    def __str__(self): return f"{self.base}*"
    def toLLVM(self): return PointerType(self.base.toLLVM())
    def __len__(self): return 4
class FType(Type):
    def __init__(self, ptypes, rtype): self.ptypes, self.rtype = ptypes, rtype
    def __str__(self): 
        ptypestr = ",".join([str(t) for t in self.ptypes])
        return f"FType({ptypestr}->{self.rtype})"
    def toLLVM(self): return FunctionType(self.rtype.toLLVM(), [t.toLLVM() for t in self.ptypes])
    def __len__(self): 1
