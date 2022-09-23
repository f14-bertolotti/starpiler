from src.syntax.slang import lang
from pathlib import Path

from llvmlite import ir
from llvmlite import binding 
from lark.visitors import Visitor
from lark.visitors import Transformer
from lark.lexer import Token

import sys
import rich

from ctypes import CFUNCTYPE, c_int64

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
        for func in funcs: func[0].block.toLLVM(func[1], module)
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

class Add:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"Add({self.x},{self.y})"
    def toLLVM(self, builder, name=None):
        LValue, LType = self.x.toLLVM(builder)
        RValue, RType = self.y.toLLVM(builder)
        assert LType == RType, f"fTypes do not agree. Found left={LType}, right={RType}."
        if LType == ir.IntType(64)  : return builder. add(LValue, RValue), LType
        if LType == ir.FloatType(64): return builder.fadd(LValue, RValue), LType

class Mul:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"Mul({self.x},{self.y})"
    def toLLVM(self, builder):
        LValue, LType = self.x.toLLVM(builder)
        RValue, RType = self.y.toLLVM(builder)
        assert LType == RType, f"fTypes do not agree. Found left={LType}, right={RType}."
        if LType == ir.IntType(64)  : return builder. mul(LValue, RValue), LType
        if LType == ir.FloatType(64): return builder.fmul(LValue, RValue), LType

class Block:
    def __init__(self, *args):
        self.statements = args
    def __str__(self):
        self.stmtsstr = ",".join([str(stmt) for stmt in self.statements])
        return f"Block({self.stmtsstr})"
    def toLLVM(self, func, module):
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        builder.name2var = {arg.strname:(arg, arg.type) for arg in func.args}
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

class Decimal:
    def __init__(self, value):
        self.value = ir.Constant(ir.FloatType(64), value)
    def __str__(self):
        return f"Decimal({self.value})"
    def toLLVM(self, _):
        return self.value, ir.FloatType(64)

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

    def s_add(self, node):
        return Add(node[0], node[2])

    def s_mul(self, node):
        return Mul(node[0], node[2])

    def s_fcl(self, node):
        return FunctionCall(node[0], *[n for n in node[2:-1] if n != Name(",")])

    def s_param(self, node):
        return Parameter(node[0], node[1])

    def s_int64(self, _):
        return ir.IntType(64)

    def s_float64(self, _):
        return ir.FloatType(64)

    def s_identifier(self, node):
        return Name(node[0].value.strip())

    def s_integer(self, node):
        return Integer(node[0].value)

    def s_decimal(self, node):
        return Decimal(node[0].value)


def runProgram():
    parsed = lang.parse(Path(sys.argv[1]).read_text())
    program = SlangTransformer().transform(parsed)
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
    cfunc = CFUNCTYPE(c_int64)(func_ptr)
    res = cfunc()
    print(res)

runProgram()
