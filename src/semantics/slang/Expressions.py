
from src.semantics.slang import Int8, Int32, Int64, Double, Pointer, FType
from abc import abstractmethod
from llvmlite import ir
from functools import partial

class Expression:
    @abstractmethod
    def getType(self, builder): pass 

class FunctionCall(Expression):
    def __init__(self, expr, args):
        self.expr = expr
        self.arguments = args
    def __str__(self):
        argsstr = ",".join([str(arg) for arg in self.arguments])
        return f"Call({self.expr},{argsstr})"
    def getType(self, builder):
        return self.expr.getType(builder).base.rtype
    def toLLVM(self, builder):
        callable = self.expr.toLLVM(builder)
        arguments = [arg.toLLVM(builder) for arg in self.arguments]
        return builder.call(callable, arguments)

class Operation(Expression):
    @abstractmethod
    def getOperation(self, builder): pass

    def raiseOperationNotFound(self, builder):
        raise ValueError(f"non suitable operation for type {self.getType(builder)}")

class BinaryOperation(Operation):
    def __init__(self, x, y):
        self.x, self.y = x, y

    @abstractmethod
    def getOperation(self, builder): pass

    def getType(self, builder): 
        ltype = self.x.getType(builder)
        rtype = self.y.getType(builder)
        if ltype == rtype: return ltype
        raise ValueError(f"non coherent types. Found left:{ltype}, right:{rtype}")
    def __str__(self):
        return f"{self.__class__.__name__}({self.x},{self.y})"
    def toLLVM(self, builder):
        lexpr = self.x.toLLVM(builder)
        rexpr = self.y.toLLVM(builder)
        return self.getOperation(builder)(lexpr, rexpr)


class UnaryOperation(Operation):
    def __init__(self, x):
        self.x = x

    def getType(self, builder): return self.x.getType(builder)

    @abstractmethod
    def getOperation(self, builder): pass

    def __str__(self):
        return f"{self.__class__.__name__}({self.x})"
    def toLLVM(self, builder):
        return self.getOperation(builder)(self.x.toLLVM(builder))

class ComparisonOperation(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self, x, y)
    
    @abstractmethod
    def getOperation(self, builder): pass

    def toLLVM(self, builder):
        lexpr = self.x.toLLVM(builder)
        rexpr = self.y.toLLVM(builder)
        return builder.select(self.getOperation(builder)(lexpr, rexpr), ir.Constant(ir.IntType(64),1), ir.Constant(ir.IntType(64),0))

class Add(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if   self.getType(builder) == Int64(): return builder.add
        elif self.getType(builder) == Double(): return builder.fadd
        self.raiseOperationNotFound(builder)

class Sub(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y)
    def getOperation(self,builder):
        if   self.getType(builder) == Int64(): return builder.sub
        elif self.getType(builder) == Double(): return builder.fsub
        self.raiseOperationNotFound(builder)

class Mul(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y)
    def getOperation(self,builder):
        if   self.getType(builder) == Int64(): return builder.mul
        elif self.getType(builder) == Double(): return builder.fmul
        self.raiseOperationNotFound(builder)

class Div(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if   self.getType(builder) == Int64(): return builder.sdiv
        elif self.getType(builder) == Double(): return builder.fdiv
        self.raiseOperationNotFound(builder)

class Mod(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if   self.getType(builder) == Int64(): return builder.srem
        elif self.getType(builder) == Double(): return builder.frem
        self.raiseOperationNotFound(builder)

class Neg(UnaryOperation):
    def __init__(self, x):
        UnaryOperation.__init__(self,x)
    def getOperation(self, builder):
        if   self.getType(builder) == Int64(): return builder.neg
        elif self.getType(builder) == Double(): return builder.fneg
        self.raiseOperationNotFound(builder)

class SizeOf(UnaryOperation):
    def __init__(self, x):
        UnaryOperation.__init__(self, x)
    def getType(self,builder): return Int64();
    def toLLVM(self, builder):
        const0 = ir.Constant(ir.IntType(64),0)
        nullptr = builder.inttoptr(const0, self.x.toLLVM(builder.module).as_pointer())
        ptrsize = builder.gep(nullptr, [ir.Constant(ir.IntType(32),1)])
        size = builder.ptrtoint(ptrsize, ir.IntType(64))
        return size



class Cast(Expression):
    def __init__(self, expr, type):
        self.type, self.expr = type, expr
    def __str__(self):
        return f"Cast({self.type},{self.expr})"
    def getType(self, _):
        return self.type
    def toLLVM(self, builder):
        expr, etype = self.expr.toLLVM(builder), self.expr.getType(builder)
        if isinstance(etype, Pointer) and     isinstance(self.type, Pointer): return builder.bitcast (expr, self.type.toLLVM(builder.module))
        if isinstance(etype, Pointer) and not isinstance(self.type, Pointer): return builder.ptrtoint(expr, self.type.toLLVM(builder.module))
        if not isinstance(etype, Pointer) and isinstance(self.type, Pointer): return builder.inttoptr(expr, self.type.toLLVM(builder.module))
        if etype == Int64() and self.type in {Int32(), Int8()}  : return builder.trunc(expr, self.type.toLLVM(builder.module))
        if etype == Int32() and self.type in {Int8()}           : return builder.trunc(expr, self.type.toLLVM(builder.module))
        if etype == Int8()  and self.type in {Int32(), Int64()} : return builder.zext (expr, self.type.toLLVM(builder.module))
        if etype == Int32() and self.type in {Int64()}          : return builder.zext (expr, self.type.toLLVM(builder.module))
        if etype == Double() and self.type == Int64(): return builder.fptosi(expr, self.type.toLLVM(builder.module))
        if etype in {Int32(), Int8(), Int64()} and self.type == Double(): return builder.sitofp(expr, self.type.toLLVM(builder.module))

        assert False, f"unkown cast for {expr.type} -> {self.type}"


class ValIndex: 
    def __init__(self, index): self.index = index
    def __str__(self): return f"[{self.index}]"
    def toLLVM(self, builder, val): 
        return builder.load(builder.gep(val, [self.index.toLLVM(builder)]))

class RefIndex:
    def __init__(self, index): self.index = index
    def __str__(self): return f"&[{self.index}]"
    def toLLVM(self, builder, val): 
        return builder.gep(val, [self.index.toLLVM(builder)])

class Index(Expression):
    def __init__(self, name, indexes): self.name, self.indexes = name, indexes
    def __str__(self): return f"Index({self.name},"+"".join([str(idx) for idx in self.indexes])+")"
    def getType(self, builder):
        currentType = self.name.getType(builder)
        for idx in self.indexes: 
            if isinstance(idx,ValIndex): currentType = currentType.base
        return currentType
    def toLLVM(self, builder):
        val = self.name.toLLVM(builder)
        for idx in self.indexes: val = idx.toLLVM(builder, val)
        return val
    
class Integer(Expression):
    def __init__(self, value):
        self.value = ir.Constant(ir.IntType(64), value)
    def __str__(self):
        return f"Integer({self.value})"
    def getType(self,_): return Int64()
    def toLLVM(self, _):
        return self.value

class Rational(Expression):
    def __init__(self, value): self.value = ir.Constant(ir.DoubleType(), value)
    def __str__(self): return f"Rational({self.value})"
    def getType(self,_): return Double()
    def toLLVM(self,_): return self.value

class String(Expression):
    def __init__(self, value): 
        self.value = eval(value) + "\0" 
        self.type = ir.ArrayType(ir.IntType(8), len(self.value))
    def __str__(self): return f"String({self.value})"
    def getType(self,_): return Pointer(Int8()) 
    def toLLVM(self,builder):
        gvar = ir.GlobalVariable(builder.module, self.type, builder.module.get_unique_name())
        gvar.global_constant = True
        gvar.linkage = "internal"
        gvar.unnamed_addr = True
        gvar.align = 1
        gvar.initializer = self.type(bytearray(self.value.encode("ASCII")))
        return gvar.gep([ir.Constant(ir.IntType(64), 0), ir.Constant(ir.IntType(64), 0)])

class Array(Expression):
    def __init__(self, values):
        assert len(values) > 0, "Invalid 0 length array"
        self.values = values
    def __str__(self): 
        arrayString = ",".join([str(val) for val in self.values])
        return f"Array({arrayString})"
    def getType(self, builder): return Pointer(self.values[0].getType(builder))
    def toLLVM(self, builder):
        ptr = builder.alloca(self.getType(builder).base.toLLVM(builder.module), len(self.values))
        for i,val in enumerate(self.values): 
            pptr = builder.gep(ptr, [ir.Constant(ir.IntType(64),i)])
            vall = val.toLLVM(builder)
            builder.store(vall, pptr)
        return ptr

class Name(Expression):
    def __init__(self, value): self.value = value
    def __str__(self): return f"Name({self.value})"
    def __hash__(self): return hash(self.value)
    def __eq__(self, other): return other.value == self.value
    def __neq__(self, other): return other.value != self.value
    def getType(self, builder): return builder.name2var[self.value].type
    def toLLVM(self, builder): 
        return builder.load(builder.name2var[self.value].ref)

class Ref(Expression):
    def __init__(self, name): self.name = name
    def __str__(self): return f"Ref({self.name})"
    def getType(self, builder): return Pointer(self.name.getType(builder))
    def toLLVM(self, builder): return builder.name2var[self.name.value].ref

class Eqs(ComparisonOperation):
    def __init__(self, x, y):
        ComparisonOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if self.getType(builder) == Int64(): return partial(builder.icmp_signed, "==")
        if self.getType(builder) == Double(): return partial(builder.fcmp_ordered, "==")
        self.raiseOperationNotFound(builder)

class Gtr(ComparisonOperation):
    def __init__(self, x, y):
        ComparisonOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if self.getType(builder) == Int64(): return partial(builder.icmp_signed, ">")
        if self.getType(builder) == Double(): return partial(builder.fcmp_unordered, ">")
        self.raiseOperationNotFound(builder)

class Gte(ComparisonOperation):
    def __init__(self, x, y):
        ComparisonOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if self.getType(builder) == Int64(): return partial(builder.icmp_signed, ">=")
        if self.getType(builder) == Double(): return partial(builder.fcmp_unordered, ">=")
        self.raiseOperationNotFound(builder)

class Lss(ComparisonOperation):
    def __init__(self, x, y):
        ComparisonOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if self.getType(builder) == Int64(): return partial(builder.icmp_signed, "<")
        if self.getType(builder) == Double(): return partial(builder.fcmp_unordered, "<")
        self.raiseOperationNotFound(builder)

class Lse(ComparisonOperation):
    def __init__(self, x, y):
        ComparisonOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if self.getType(builder) == Int64(): return partial(builder.icmp_signed, "<=")
        if self.getType(builder) == Double(): return partial(builder.fcmp_unordered, "<=")
        self.raiseOperationNotFound(builder)

class Neq(ComparisonOperation):
    def __init__(self, x, y):
        ComparisonOperation.__init__(self,x,y)
    def getOperation(self, builder):
        if self.getType(builder) == Int64(): return partial(builder.icmp_signed, "!=")
        if self.getType(builder) == Double(): return partial(builder.fcmp_unordered, "!=")
        self.raiseOperationNotFound(builder)

class StructNameDeclaration: 
    def __init__(self, type, name): self.type, self.name = type, name
    def __str__(self): return f"StructNameDeclaration({self.name},{self.type})"
    def toLLVM(self, builder): pass

class StructNameDefinition: 
    def __init__(self, type, name, expr): self.type, self.name, self.expr = type, name, expr
    def __str__(self): return f"StructNameDefinition({self.type},{self.name},{self.expr})"
    def toLLVM(self, builder):
        ptr = builder.alloca(self.type.toLLVM(builder))
        val = self.expr.toLLVM(builder)
        builder.store(val,ptr)

class StructValue(Expression):
    def __init__(self, name, names, expressions): 
        self.structName = name
        self.name2expr = dict(zip(names, expressions))

    def __str__(self):
        values = ",".join([f"{str(n)}:{str(e)}" for n,e in self.name2expr.values()])
        return f"Struct({self.structName.value},{values})"
    def getType(self, builder): return Pointer(builder.name2var[self.structName.value].type)
    def toLLVM(self, builder):
        name2expr = {inner.name:inner.expr for inner in builder.name2var[self.structName.value].innerNames if isinstance(inner, StructNameDefinition)}
        name2expr.update(self.name2expr)
        ptr = builder.alloca(builder.name2var[self.structName.value].ref)
        tmp, builder.name2var = builder.name2var, {**builder.module.path2import[builder.name2var[self.structName.value].type.path], **builder.name2var}
        for name,expr in name2expr.items():
            idx = [inner.name for inner in builder.name2var[self.structName.value].innerNames].index(name)
            pptr = builder.gep(ptr, [ir.Constant(ir.IntType(64),0), ir.Constant(ir.IntType(32), idx)])
            builder.store(expr.toLLVM(builder), pptr)
            builder.name2var.update({name.value:type("__ANON__",tuple(),{"ref":pptr,"type":expr.getType(builder)})()})
        builder.name2var = tmp
        return ptr;

class StructAccess(Expression):
    def __init__(self, accessed, index): self.accessed, self.index = accessed, index
    def __str__(self): return f"Access({self.accessed},{self.index})"
    def getType(self, builder): return self.accessed.getType(builder).base.typeof(builder.module, self.index)
    def toLLVM(self, builder):
        expr = self.accessed.toLLVM(builder)
        idx = self.accessed.getType(builder).base.index(builder.module, self.index)
        ptr = builder.gep(expr, [ir.Constant(ir.IntType(64),0), ir.Constant(ir.IntType(32), idx)])
        return builder.load(ptr)

class StructRefAccess(Expression):
    def __init__(self, accessed, index): self.accessed, self.index = accessed, index
    def __str__(self): return f"Access({self.accessed},{self.index})"
    def getType(self, builder): 
        return self.accessed.getType(builder).base.typeof(builder.module, self.index)
    def toLLVM(self, builder):
        expr = self.accessed.toLLVM(builder)
        idx = self.accessed.getType(builder).base.index(builder.module, self.index)
        return builder.gep(expr, [ir.Constant(ir.IntType(64),0), ir.Constant(ir.IntType(32), idx)])


