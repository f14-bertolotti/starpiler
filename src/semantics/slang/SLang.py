from src.syntax.slang import lang

from llvmlite import ir
from llvmlite import binding 
from lark.visitors import Transformer
from lark import Token
import copy

from ctypes import CFUNCTYPE, CDLL, c_void_p, c_double, c_int64
import ctypes
from ctypes.util import find_library

from collections import defaultdict
from functools import partial

import abc

class Type: 
    @abc.abstractmethod
    def LLVMType(self): pass
    def __eq__(self, other): return str(self) == str(other) 
    def __neq__(self, other):return str(self) != str(other)
    def __hash__(self): return hash(self.__class__)
class Void(Type):
    def LLVMType(self): return ir.VoidType()
    def __str__(self): return "Void"
class Int8(Type): 
    def LLVMType(self): return ir.IntType(8)
    def __str__(self): return "Int8"
class Int32(Type):
    def LLVMType(self): return ir.IntType(32)
    def __str__(self): return "Int32"
class Int64(Type): 
    def LLVMType(self): return ir.IntType(64)
    def __str__(self): return "Int64"  
class Double(Type): 
    def LLVMType(self): return ir.DoubleType()
    def __str__(self): return "Double"
class Array(Type):
    def __init__(self, base, length): self.base, self.length = base, length
    def LLVMType(self): return ir.ArrayType(self.base.LLVMType(), self.length)
    def __Str__(self): return f"Array({self.base},{self.length})"
class Pointer(Type):
    def __init__(self, base): self.base = base
    def __str__(self): return f"{self.base}*"
    def LLVMType(self): return ir.PointerType(self.base.LLVMType())

const64_0 = ir.Constant(ir.IntType(64), 0)
const64_1 = ir.Constant(ir.IntType(64), 1)

class Parameter:
    def __init__(self, type, name):
        self.type, self.name = type, name
    def __str__(self):
        return f"Parameter({self.type},{self.name})"

class ParameterSequence:
    def __init__(self, *args):
        self.parameters = args
    def __get_item__(self, index):
        return self.parameters[index]
    def __iter__(self):
        return iter(self.parameters)
    def __str__(self):
        paramsstr = ",".join(str(param) for param in self.parameters)
        return f"ParameterSequence({paramsstr})"

class Module:
    def __init__(self, functions):
        self.functions = functions 
    def __str__(self):
        funcstr = ",".join([str(func) for func in self.functions])
        return f"Module({funcstr})"
    def toLLVM(self):
        module = ir.Module(name="MainModule")

        functionType = ir.FunctionType(ir.IntType(8).as_pointer(), [ir.IntType(64)])
        function = ir.Function(module, functionType, name="malloc")
        function.returnType = Pointer(Int8())
        
        functionType = ir.FunctionType(ir.VoidType(), [ir.IntType(8).as_pointer()])
        function = ir.Function(module, functionType, name="free")
        function.returnType = Void()

        functionType = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()], var_arg=True)
        function = ir.Function(module, functionType, name="printf")
        function.returnType = Int32()

        funcs = [(func, func.toLLVM(module)) for func in self.functions]
        for func in funcs: 
            block = func[1].append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            builder.name2var = {param.name.value:(builder.alloca(param.type.LLVMType()), param.type) for param in func[0].parameters}
            for arg in func[1].args: builder.store(arg, builder.name2var[arg.strname][0])
            func[0].block.toLLVM(builder)
        return module

class Function:
    def __init__(self, returnType, name, parameters, block):
        self.returnType = returnType
        self.parameters = parameters
        self.block = block
        self.name = name
    def __str__(self):
        return f"Function({self.returnType},{self.name},{self.parameters},{self.block})"
    def toLLVM(self, module):
        functionType = ir.FunctionType(self.returnType.LLVMType(), [param.type.LLVMType() for param in self.parameters])
        function = ir.Function(module, functionType, name=self.name.value)
        function.returnType = self.returnType
        for param, arg in zip(self.parameters, function.args): arg.strname = param.name.value
        return function

class Expression:
    @abc.abstractmethod
    def getType(self, builder): pass 

class FunctionCall(Expression):
    def __init__(self, name, *args):
        self.name = name
        self.arguments = args
    def __str__(self):
        argsstr = ",".join([str(arg) for arg in self.arguments])
        return f"Call({self.name},{argsstr})"
    def getType(self, builder):
        func = [f for f in builder.module.functions if f.name == self.name.value][-1]
        return func.returnType
    def toLLVM(self, builder):
        func = [f for f in builder.module.functions if f.name == self.name.value][-1]
        return builder.call(func, [arg.toLLVM(builder) for arg in self.arguments])

class Operation(Expression):
    @abc.abstractmethod
    def getOperation(self, builder): pass

    def raiseOperationNotFound(self, builder):
        raise ValueError(f"non suitable operation for type {self.getType(builder)}")

class BinaryOperation(Operation):
    def __init__(self, x, y):
        self.x, self.y = x, y

    @abc.abstractmethod
    def getOperation(self, builder): pass

    def getLType(self, builder): return self.x.getType(builder)

    def getRType(self, builder): return self.y.getType(builder)

    def getType(self, builder): 
        ltype = self.getLType(builder)
        rtype = self.getRType(builder)
        if ltype == rtype: return ltype
        assert ltype == rtype,  f"non coherent types. Found left:{ltype}, right:{rtype}"
        return ltype

    def __str__(self):
        dir(self)
        return f"{self.__class__.__name__}({self.x},{self.y})"
    def toLLVM(self, builder):
        lexpr = self.x.toLLVM(builder)
        rexpr = self.y.toLLVM(builder)
        return self.getOperation(builder)(lexpr, rexpr)


class UnaryOperation(Operation):
    def __init__(self, x):
        self.x = x

    def getType(self, builder): return self.x.getType(builder)

    @abc.abstractmethod
    def getOperation(self, builder): pass

    def __str__(self):
        return f"{self.__class__.__name__}({self.x})"
    def toLLVM(self, builder):
        return self.getOperation(builder)(self.x.toLLVM(builder))

class ComparisonOperation(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self, x, y)
    
    @abc.abstractmethod
    def getOperation(self, builder): pass

    def toLLVM(self, builder):
        lexpr = self.x.toLLVM(builder)
        rexpr = self.y.toLLVM(builder)
        return builder.select(self.getOperation(builder)(lexpr, rexpr), const64_1, const64_0)

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

class Cast(Expression):
    def __init__(self, expr, type):
        self.type, self.expr = type, expr
    def __str__(self):
        return f"Cast({self.type},{self.expr})"
    def getType(self, _):
        return self.type.LLVMType()
    def toLLVM(self, builder):
        expr, etype = self.expr.toLLVM(builder), self.expr.getType(builder)
        if isinstance(etype, Pointer) and     isinstance(self.type, Pointer): return builder.bitcast (expr, self.type.LLVMType())
        if isinstance(etype, Pointer) and not isinstance(self.type, Pointer): return builder.ptrtoint(expr, self.type.LLVMType())
        if not isinstance(etype, Pointer) and isinstance(self.type, Pointer): return builder.inttoptr(expr, self.type.LLVMType())
        if etype == Int64() and self.type in {Int32(), Int8()}  : return builder.trunc(expr, self.type.LLVMType())
        if etype == Int32() and self.type in {Int8()}           : return builder.trunc(expr, self.type.LLVMType())
        if etype == Int8()  and self.type in {Int32(), Int64()} : return builder.zext (expr, self.type.LLVMType())
        if etype == Int32() and self.type in {Int64()}          : return builder.zext (expr, self.type.LLVMType())


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
    def __str__(self): return f"{self.name}["+",".join([str(idx) for idx in self.indexes])+"]"
    def getType(self, builder):
        currentType = self.name.getType(builder)
        for _ in self.indexes: currentType = currentType.base
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
        self.value = value[1:-1] + "\0" 
        self.type = ir.ArrayType(ir.IntType(8), len(self.value))
    def __str__(self): return f"Rational({self.value})"
    def getType(self,_): return Pointer(Int8()) 
    def toLLVM(self,builder):
        gvar = ir.GlobalVariable(builder.module, self.type, builder.module.get_unique_name())
        gvar.global_constant = True
        gvar.linkage = "internal"
        gvar.unnamed_addr = True
        gvar.align = 1
        gvar.initializer = self.type(bytearray(self.value.encode("utf8")))
        return gvar.gep([const64_0, const64_0])

class Name(Expression):
    def __init__(self, value): self.value = value
    def __str__(self): return f"Name({self.value})"
    def getType(self, builder): return builder.name2var[self.value][1]
    def toLLVM(self, builder): return builder.load(builder.name2var[self.value][0])

class Ref(Expression):
    def __init__(self, expr): self.expr = expr
    def __str__(self): return f"Ref({self.expr})"
    def getType(self, builder): return Pointer(self.expr.getType(builder))
    def toLLVM(self, builder): return builder.name2var[self.expr.value][0]

class Load(Expression):
    def __init__(self, expr): self.expr = expr
    def __str__(self): return f"Load({self.expr})"
    def getType(self, builder): return self.expr.getType(builder).base
    def toLLVM(self, builder): 
        expr = self.expr.toLLVM(builder)
        assert isinstance(expr.type, ir.PointerType)
        return builder.load(expr)

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

class Block:
    def __init__(self, *args):
        self.statements = args
    def __str__(self):
        self.stmtsstr = ",".join([str(stmt) for stmt in self.statements])
        return f"Block({self.stmtsstr})"
    def toLLVM(self, builder):
        for stmt in self.statements: 
            stmt.toLLVM(builder)

class DeclareAssign:
    def __init__(self, type, name, expr):
        self.type, self.name, self.expr = type, name, expr
    def __str__(self):
        return f"Ass({self.type},{self.name},{self.expr})"
    def toLLVM(self, builder):
        expr = self.expr.toLLVM(builder)
        var = builder.alloca(self.type.LLVMType())

        builder.store(expr, var)
        builder.name2var[self.name.value] = (var, self.type)

class ReAssign:
    def __init__(self, lexpr, rexpr):
        self.lexpr, self.rexpr = lexpr, rexpr
    def __str__(self):
        return f"RAss({self.lexpr},{self.rexpr})"
    def toLLVM(self, builder):
        rexpr = self.rexpr.toLLVM(builder)
        lexpr = self.lexpr.toLLVM(builder)
        builder.store(rexpr, lexpr)

class Skip:
    def __init__(self): pass
    def __str__(self): return f"Skip"
    def toLLVM(self, _): pass

class IfThen:
    def __init__(self, cond, block): self.cond, self.block = cond, block
    def __str__(self): return f"IfThen({self.cond},{self.block})"
    def toLLVM(self, builder):
        cond = builder.icmp_signed("==",self.cond.toLLVM(builder), const64_1)
        tmp = builder.name2var
        builder.name2var = copy.deepcopy(builder.name2var)
        with builder.if_then(cond):
            self.block.toLLVM(builder)
        builder.name2var = tmp

class While:
    def __init__(self, cond, block): self.cond, self.block = cond, block
    def __str__(self): return f"While({self.cond},{self.block})"
    def toLLVM(self, builder):

        whileblock = builder.function.append_basic_block()
        endblock   = builder.function.append_basic_block()
        bodyblock  = builder.function.append_basic_block()

        whilebuilder = ir.IRBuilder(whileblock)
        bodybuilder  = ir.IRBuilder(bodyblock)
        whilebuilder.name2var = builder.name2var
        bodybuilder .name2var = copy.deepcopy(builder.name2var)

        builder.branch(whileblock)
    
        cond = whilebuilder.icmp_signed("==", self.cond.toLLVM(whilebuilder), const64_1)
        whilebuilder.cbranch(cond, bodyblock, endblock)

        self.block.toLLVM(bodybuilder)
        bodybuilder.branch(whileblock)

        builder.position_at_start(endblock)

class Return:
    def __init__(self, expr):
        self.expr = expr
    def __str__(self):
        return f"Return({self.expr})"
    def toLLVM(self, builder):
        res = self.expr.toLLVM(builder)
        if isinstance(res.type, ir.PointerType): builder.ret(builder.load(res))
        else: builder.ret(res)

class SlangTransformer(Transformer):

    def start(self, node):
        return Module(node)

    def s_param_seq(self, node): 
        return ParameterSequence(*[param for param in node if isinstance(param,Parameter)])

    def s_func(self, node):
        return Function(node[1], node[2], node[3], node[5])

    def s_block(self, node):
        return Block(*node)

    def s_return(self, node):
        return Return(node[1])

    def s_decl_assign(self, node):
        return DeclareAssign(node[0], node[1], node[3])

    def s_nodecl_assign(self, node):
        return ReAssign(node[0], node[2])
    
    def s_ifthen(self, node):
        return IfThen(node[1], node[3])

    def s_while(self, node):
        return While(node[1], node[3])

    def s_statement(self, node):
        return node[0]

    def s_add(self, node): return Add(node[0], node[2])
    def s_sub(self, node): return Sub(node[0], node[2])
    def s_mul(self, node): return Mul(node[0], node[2])
    def s_div(self, node): return Div(node[0], node[2])
    def s_mod(self, node): return Mod(node[0], node[2])
    def s_eql(self, node): return Eqs(node[0], node[2])
    def s_gtr(self, node): return Gtr(node[0], node[2])
    def s_gte(self, node): return Gte(node[0], node[2])
    def s_lss(self, node): return Lss(node[0], node[2])
    def s_lse(self, node): return Lse(node[0], node[2])
    def s_neq(self, node): return Neq(node[0], node[2])
    def s_neg(self, node): return Neg(node[1])
    def s_fcl(self, node): return FunctionCall(node[0], *[n for n in node[2].children if not isinstance(n,Token)])

    def s_skip(self, _):
        return Skip();

    def s_param(self, node):
        return Parameter(node[0], node[1])

    def s_int64(self, _):
        return Int64()

    def s_int8(self, _):
        return Int8()

    def s_float64(self, _):
        return Double()

    def s_identifier(self, node):
        return Name(node[0].value.strip())

    def s_ref(self, node):
        return Ref(node[1])

    def s_lad(self, node):
        return Load(node[2])

    def s_integer(self, node):
        return Integer(node[0].value)

    def s_string(self, node):
        return String(node[0].value)

    def s_rational(self, node):
        return Rational(node[0].value)

    def s_ptr(self, node):
        return Pointer(node[0])

    def s_cst(self, node):
        return Cast(node[0], node[2])

    def s_sqt(self, node):
        return ValIndex(node[1])

    def s_rqt(self, node):
        return RefIndex(node[1])

    def s_idx(self, node):
        return Index(node[0], node[1:])



import rich

def parsed(programstr):
    #rich.print(programstr)
    res = lang.parse(programstr)
    #rich.print(res)
    return res

def transformed(programstr):
    return SlangTransformer().transform(parsed(programstr))

def assembled(programstr):
    return str(transformed(programstr).toLLVM())

def run(programstr):
    program = transformed(programstr) 
    #rich.print(program)

    module = program.toLLVM()
    #print(module)
    
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()
    binding.load_library_permanently(ctypes.util.find_library('c'))

    parsedAssembly = binding.parse_assembly(str(module))
    parsedAssembly.verify()
    
    target = binding.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = binding.parse_assembly("")
    engine = binding.create_mcjit_compiler(backing_mod, target_machine)
    
    engine.add_module(parsedAssembly)
    engine.finalize_object()
    engine.run_static_constructors()
    
    func_ptr = engine.get_function_address("start")
    rtype = [func.returnType for func in program.functions if func.name.value == "start"][-1]
    if rtype == Double(): cfunc = CFUNCTYPE(c_double)(func_ptr)
    if rtype == Int64(): cfunc = CFUNCTYPE(c_int64)(func_ptr)
    res = cfunc()
    return res

