from abc import abstractmethod
from llvmlite.ir import VoidType, IntType, DoubleType, PointerType, FunctionType, LiteralStructType


class Type: 
    abstractmethod
    def toLLVM(self): pass
    abstractmethod
    def __len__(self): pass
    def __eq__(self, other): return str(self) == str(other) 
    def __neq__(self, other):return str(self) != str(other)
    def __hash__(self): return hash(self.__class__)
class Void(Type):
    def toLLVM(self,_): return VoidType()
    def __str__(self): return "Void"
    def __len__(self): raise ValueError("Void Type has no size")
class Int8(Type): 
    def toLLVM(self,_): return IntType(8)
    def __str__(self): return "Int8"
    def __len__(self): return 1
class Int32(Type):
    def toLLVM(self,_): return IntType(32)
    def __str__(self): return "Int32"
    def __len__(self): return 2
class Int64(Type): 
    def toLLVM(self,_): return IntType(64)
    def __str__(self): return "Int64"  
    def __len__(self): return 4
class Double(Type): 
    def toLLVM(self,_): return DoubleType()
    def __str__(self): return "Double"
    def __len__(self): return 8
class Pointer(Type):
    def __init__(self, base): self.base = base
    def __str__(self): return f"{self.base}*"
    def toLLVM(self,module): return PointerType(self.base.toLLVM(module))
    def __len__(self): return 4
class FType(Type):
    def __init__(self, ptypes, rtype, vararg=False): self.ptypes, self.rtype, self.vararg = ptypes, rtype, vararg
    def __str__(self): 
        ptypestr = ",".join([str(t) for t in self.ptypes])
        return f"FType({ptypestr}->{self.rtype})"
    def toLLVM(self,module): return FunctionType(self.rtype.toLLVM(module), [t.toLLVM(module) for t in self.ptypes], var_arg = self.vararg)
    def __len__(self): 1
class SType(Type):
    def __init__(self, name): self.name = name
    def __str__(self): return f"{self.name}"
    def index(self, module, value): return module.name2decl[self.name].names.index(value)
    def typeof(self, module, value): return module.name2decl[self.name].types[self.index(module, value)]
    def toLLVM(self,module): 
        return module.name2decl[self.name].ref
