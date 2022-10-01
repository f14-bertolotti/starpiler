from abc import abstractmethod
from llvmlite.ir import VoidType, IntType, DoubleType, PointerType


class Type: 
    abstractmethod
    def asLLVM(self): pass
    abstractmethod
    def __len__(self): pass
    def __eq__(self, other): return str(self) == str(other) 
    def __neq__(self, other):return str(self) != str(other)
    def __hash__(self): return hash(self.__class__)
class Void(Type):
    def asLLVM(self): return VoidType()
    def __str__(self): return "Void"
    def __len__(self): raise ValueError("Void Type has no size")
class Int8(Type): 
    def asLLVM(self): return IntType(8)
    def __str__(self): return "Int8"
    def __len__(self): return 1
class Int32(Type):
    def asLLVM(self): return IntType(32)
    def __str__(self): return "Int32"
    def __len__(self): return 2
class Int64(Type): 
    def asLLVM(self): return IntType(64)
    def __str__(self): return "Int64"  
    def __len__(self): return 4
class Double(Type): 
    def asLLVM(self): return DoubleType()
    def __str__(self): return "Double"
    def __len__(self): return 8
class Pointer(Type):
    def __init__(self, base): self.base = base
    def __str__(self): return f"{self.base}*"
    def asLLVM(self): return PointerType(self.base.asLLVM())
    def __len__(self): return 4

