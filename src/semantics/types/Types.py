
class Type:
    def __eq__(self, other): return str(self) == str(other)
    def __neq__(self, other): return str(self) != str(other)
class Void(Type):
    def __str__(self): return "void"
class Int8(Type): 
    def __str__(self): return "int8"
class Int32(Type):
    def __str__(self): return "int32"
class Int64(Type): 
    def __str__(self): return "int64"  
class Double(Type): 
    def __str__(self): return "double"
class Pointer(Type):
    def __init__(self, base): self.base = base
    def __str__(self): return f"{self.base}*"
class FType(Type):
    def __init__(self, ptypes, rtype, vararg=False): self.ptypes, self.rtype, self.vararg = ptypes, rtype, vararg
    def __str__(self): 
        ptypestr = ",".join([str(t) for t in self.ptypes])
        return f"({ptypestr}->{self.rtype})"
class SType(Type):
    def __init__(self, name, name2type): self.name, self.name2type = name, name2type
    def __contains__(self, name): return name in self.name2type
    def __getitem__(self, name): return self.name2type[name]
    def __str__(self): 
        name2type_str = "{" + ",".join([f"{k}:{v}" for k,v in self.name2type.items()]) + "}"
        return f"{self.name}{name2type_str}"
    def isValid(self, name2type): return all(name2type[name] == self.name2type[name] for name in name2type)
