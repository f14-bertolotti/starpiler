from src.syntax.slang import lang

from llvmlite import ir
from llvmlite import binding 
from lark.visitors import Transformer
import copy

from ctypes import CFUNCTYPE, c_double, c_int64

class Parameter:
    def __init__(self, type, name):
        self.type, self.name = type, name
    def __str__(self):
        return f"Parameter({self.type},{self.name})"

class ParameterSequence:
    def __init__(self, *args):
        self.paramters = args
    def __get_item__(self, index):
        return self.paramters[index]
    def __iter__(self):
        return iter(self.paramters)
    def __str__(self):
        paramsstr = ",".join(str(param) for param in self.paramters)
        return f"ParameterSequence({paramsstr})"

class Module:
    def __init__(self, functions):
        self.functions = functions 
    def __str__(self):
        funcstr = ",".join([str(func) for func in self.functions])
        return f"Module({funcstr})"
    def toLLVM(self):
        module = ir.Module(name="MainModule")
        funcs = [(func, func.toLLVM(module)) for func in self.functions]
        for func in funcs: 
            block = func[1].append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            builder.name2var = {arg.strname:(arg, arg.type) for arg in func[1].args}
            func[0].block.toLLVM(builder)
        return module

class Function:
    def __init__(self, returntype, name, paramters, block):
        self.returntype = returntype
        self.paramters = paramters
        self.block = block
        self.name = name
    def __str__(self):
        return f"Function({self.returntype},{self.name},{self.paramters},{self.block})"
    def toLLVM(self, module):
        functionType = ir.FunctionType(self.returntype, [param.type for param in self.paramters])
        function = ir.Function(module, functionType, name=self.name.value)
        for param, arg in zip(self.paramters, function.args): arg.strname = param.name.value
        return function

class FunctionCall:
    def __init__(self, name, *args):
        self.name = name
        self.arguments = args
    def __str__(self):
        argsstr = ",".join([str(arg) for arg in self.arguments])
        return f"Call({self.name},{argsstr})"
    def toLLVM(self, builder):
        func = [f for f in builder.module.functions if f.name == self.name.value][-1]
        return builder.call(func, [arg.toLLVM(builder)[0] for arg in self.arguments]), func.return_value

class BinaryOperation:
    def __init__(self, x, y, type2op, cmpop=None):
        self.x, self.y = x, y
        self.type2op = type2op
        self.cmpop = cmpop
    def __str__(self):
        dir(self)
        return f"{self.__class__.__name__}({self.x},{self.y})"
    def toLLVM(self, builder):
        LValue, LType = self.x.toLLVM(builder)
        RValue, RType = self.y.toLLVM(builder)
        assert LType == RType, f"fTypes do not agree. Found left={LType}, right={RType}."
        return (getattr(builder, self.type2op[LType])(self.cmpop, LValue, RValue), LType) if self.cmpop else \
               (getattr(builder, self.type2op[LType])(LValue, RValue), LType)

class UnaryOperation:
    def __init__(self, x, type2op):
        self.x = x
        self.type2op = type2op
    def __str__(self):
        dir(self)
        return f"{self.__class__.__name__}({self.x})"
    def toLLVM(self, builder):
        LValue, LType = self.x.toLLVM(builder)
        return getattr(builder, self.type2op[LType])(LValue), LType

class Add(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y,{ir.IntType(64):"add", ir.DoubleType():"fadd"})

class Sub(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y,{ir.IntType(64):"sub", ir.DoubleType():"fsub"})

class Mul(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y,{ir.IntType(64):"mul", ir.DoubleType():"fmul"})

class Div(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y,{ir.IntType(64):"sdiv", ir.DoubleType():"fdiv"})

class Neg(UnaryOperation):
    def __init__(self, x):
        UnaryOperation.__init__(self,x,{ir.IntType(64):"neg", ir.DoubleType():"fneg"})

class Mod(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y,{ir.IntType(64):"srem", ir.DoubleType():"frem"})

class Eqs(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y,{ir.IntType(64):"icmp_signed", ir.DoubleType():"fcmp_ordered"}, cmpop="==")
    def toLLVM(self, builder):
        LValue, LType = self.x.toLLVM(builder)
        RValue, RType = self.y.toLLVM(builder)
        assert LType == RType, f"fTypes do not agree. Found left={LType}, right={RType}."
        if LType == ir.IntType(64) : return builder.select(builder.icmp_signed ("==",LValue,RValue),ir.Constant(ir.IntType(64),1), ir.Constant(ir.IntType(64),0)), LType
        if LType == ir.DoubleType(): return builder.select(builder.fcmp_ordered("==",LValue,RValue),ir.Constant(ir.IntType(64),1), ir.Constant(ir.IntType(64),0)), LType

class Neq(BinaryOperation):
    def __init__(self, x, y):
        BinaryOperation.__init__(self,x,y,{ir.IntType(64):"icmp_signed", ir.DoubleType():"fcmp_ordered"}, cmpop="==")
    def toLLVM(self, builder):
        LValue, LType = self.x.toLLVM(builder)
        RValue, RType = self.y.toLLVM(builder)
        assert LType == RType, f"fTypes do not agree. Found left={LType}, right={RType}."
        if LType == ir.IntType(64) : return builder.select(builder.icmp_signed ("!=",LValue,RValue),ir.Constant(ir.IntType(64),1), ir.Constant(ir.IntType(64),0)), LType
        if LType == ir.DoubleType(): return builder.select(builder.fcmp_ordered("!=",LValue,RValue),ir.Constant(ir.IntType(64),1), ir.Constant(ir.IntType(64),0)), LType

class Block:
    def __init__(self, *args):
        self.statements = args
    def __str__(self):
        self.stmtsstr = ",".join([str(stmt) for stmt in self.statements])
        return f"Block({self.stmtsstr})"
    def toLLVM(self, builder):
        for stmt in self.statements: stmt.toLLVM(builder)

class Assign:
    def __init__(self, type, name, expr):
        self.type, self.name, self.expr = type, name, expr
    def __str__(self):
        return f"Ass({self.type},{self.name},{self.expr})"
    def toLLVM(self, builder):
        res = self.expr.toLLVM(builder)
        res[0].name = self.name.value
        builder.name2var[self.name.value] = (res[0], self.type)

class Skip:
    def __init__(self): pass
    def __str__(self): return f"Skip"
    def toLLVM(self, builder): pass

class IfThen:
    def __init__(self, cond, block): self.cond, self.block = cond, block
    def __str__(self): return f"IfThen({self.cond},{self.block})"
    def toLLVM(self, builder):

        cond = builder.icmp_signed("==",self.cond.toLLVM(builder)[0], ir.Constant(ir.IntType(64),1))
        with builder.if_then(cond):
            self.block.toLLVM(builder)
        #self.end.toLLVM(builder)

        #tblock = builder.function.append_basic_block()
        #fblock = builder.function.append_basic_block()
        #eblock = builder.function.append_basic_block()

        #tbuilder = ir.IRBuilder(tblock)
        #fbuilder = ir.IRBuilder(fblock)
        #ebuilder = ir.IRBuilder(eblock)

        #tbuilder.name2var = copy.deepcopy(builder.name2var)
        #fbuilder.name2var = copy.deepcopy(builder.name2var)
        #ebuilder.name2var = builder.name2var 

        #self.block.toLLVM(tbuilder)
        #self.end  .toLLVM(ebuilder)

        #cond = self.cond.toLLVM(builder)
        #builder.cbranch(cond,tblock,fblock)
        #tbuilder.branch(eblock)
        #fbuilder.branch(eblock)



class Return:
    def __init__(self, expr):
        self.expr = expr
    def __str__(self):
        return f"Return({self.expr})"
    def toLLVM(self, builder):
        builder.ret(self.expr.toLLVM(builder)[0])

class Integer:
    def __init__(self, value):
        self.value = ir.Constant(ir.IntType(64), value)
    def __str__(self):
        return f"Integer({self.value})"
    def toLLVM(self, _):
        return self.value, ir.IntType(64)

class Rational:
    def __init__(self, value):
        self.value = ir.Constant(ir.DoubleType(), value)
    def __str__(self):
        return f"Rational({self.value})"
    def toLLVM(self, _):
        return self.value, ir.DoubleType()

class Name:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Name({self.value})"
    def __hash__(self):
        return hash(self.value)
    def __eq__(self, other):
        return other.value == self.value
    def __ne__(self, other):
        return other.value != self.value
    def toLLVM(self, builder):
        assert self.value in builder.name2var, f"name=\"{self.value}\" not found in current scope."
        res = builder.name2var[self.value]
        return res

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

    def s_assign(self, node):
        return Assign(node[0], node[1], node[3])

    def s_ifthen(self, node):
        return IfThen(node[1], node[3])

    def s_add(self, node): return Add(node[0], node[2])
    def s_sub(self, node): return Sub(node[0], node[2])
    def s_mul(self, node): return Mul(node[0], node[2])
    def s_div(self, node): return Div(node[0], node[2])
    def s_mod(self, node): return Mod(node[0], node[2])
    def s_eql(self, node): return Eqs(node[0], node[2])
    def s_neq(self, node): return Neq(node[0], node[2])
    def s_neg(self, node): return Neg(node[1])
    def s_fcl(self, node): return FunctionCall(node[0], *[n for n in node[2].children if n != Name(",")])

    def s_skip(self, _):
        return Skip();

    def s_param(self, node):
        return Parameter(node[0], node[1])

    def s_int64(self, _):
        return ir.IntType(64)

    def s_float64(self, _):
        return ir.DoubleType()

    def s_identifier(self, node):
        return Name(node[0].value.strip())

    def s_integer(self, node):
        return Integer(node[0].value)

    def s_rational(self, node):
        return Rational(node[0].value)

def parsed(programstr):
    return lang.parse(programstr)

def transformed(programstr):
    return SlangTransformer().transform(parsed(programstr))

def assembled(programstr):
    return str(transformed(programstr).toLLVM())

def run(programstr):
    program = transformed(programstr) 

    module = program.toLLVM()
    
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()
    
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
    rtype = [func.returntype for func in program.functions if func.name.value == "start"][-1]
    if rtype == ir.DoubleType(): cfunc = CFUNCTYPE(c_double)(func_ptr)
    if rtype == ir.IntType(64) : cfunc = CFUNCTYPE(c_int64)(func_ptr)
    res = cfunc()
    return res

