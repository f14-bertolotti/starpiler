
class Type:
    def __eq__(self, other): return type(self) == type(other)
    def __neq__(self, other): return type(self) != type(other)
    def toString(self, visited): return str(self)
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

class Array(Type):
    def __init__(self, base): self.base = base
    def __str__(self): return self.toString([])
    def toString(self, visited): 
        return f"Array({self.base.toString(visited)})"  

class Object(Type):
    def __init__(self, base): self.base = base
    def __str__(self): return self.toString([])
    def toString(self, visited): 
        return f"Object({self.base.toString(visited)})"  

class Pointer(Type):
    def __init__(self, base): self.base = base
    def __str__(self): return self.toString([])
    def toString(self, visited): 
        return f"{self.base.toString(visited)}*"  

class FType(Type):
    def __init__(self, ptypes, rtype, vararg=False): self.ptypes, self.rtype, self.vararg = ptypes, rtype, vararg
    def __str__(self): return self.toString([])
    def toString(self, visited):
        ptypestr = ",".join([t.toString(visited) for t in self.ptypes])
        if self.vararg: ptypestr += ",..." 
        return f"({ptypestr}->{self.rtype.toString(visited)})"
    def __eq__(self, other): return self is other or (type(other) == FType and self.rtype == other.rtype and self.vararg == other.vararg and all(p0==p1 for p0,p1 in zip(self.ptypes, other.ptypes)))
 
class SType(Type):
    def __init__(self, name, name2type): self.name, self.name2type = name, name2type
    def __contains__(self, name): return name in self.name2type
    def __getitem__(self, name): return self.name2type[name]
    def __setitem__(self, name, value): self.name2type[name] = value
    def __eq__(self, other): return self is other or (type(other) == SType and self.name == other.name and all(name in self.name2type and self.name2type[name] == other.name2type[name] for name in other.name2type.keys()))
    def __ne__(self, other): not (self == other)
    def toString(self, visited = list()): 
        if self in visited: 
            return str(self.name)
        else:
            visited.append(self)
            name2type_str = "{" + ",".join([f"{k}:{v.toString(visited)}" for k,v in self.name2type.items()]) + "}"
            return f"{self.name}{name2type_str}"
    def __str__(self):return self.toString(visited=[])
    def isValid(self, name2type): return all(name2type[name] == self.name2type[name] for name in name2type)
