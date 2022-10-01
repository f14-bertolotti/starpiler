from src.syntax.slang import lang

from llvmlite import ir
from llvmlite import binding 
from lark.visitors import Transformer
from lark.lexer import Token

from ctypes import CFUNCTYPE, c_double, c_int64
from ctypes.util import find_library

from src.semantics.slang import *


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
    def __init__(self, globals):
        self.globals = globals
    def __str__(self):
        string = ",".join([str(gbl) for gbl in self.globals])
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

        functionType = ir.FunctionType(ir.IntType(8).as_pointer(), [ir.IntType(8).as_pointer(), ir.IntType(8).as_pointer(), ir.IntType(32)])
        function = ir.Function(module, functionType, name="memcpy")
        function.returnType = Void()

        global2var = dict()
        for gbl in self.globals:
            if gbl.name.value in global2var: raise ValueError(f"global name already defined {gbl.name.value}")
            var = gbl.LLVMDeclaration(module)
            global2var[gbl.name.value] = (var, gbl.type)

        module.global2var = global2var
        for gbl in self.globals: gbl.toLLVM(module)
                

        startFunction = module.global2var["start"][0]
        builder = ir.IRBuilder()
        builder.position_at_start(startFunction.entry_basic_block)
        initializers = [f for f in module.functions if f.name.startswith("0initilizer")]
        for initializer in initializers: 
            value = builder.call(initializer, [])
            builder.store(value, initializer.reference) 

        return module


class Function:
    def __init__(self, type, name, parameters, block):
        self.type = type
        self.parameters = parameters
        self.block = block
        self.name = name
    def __str__(self):
        return f"Function({self.type},{self.name},{self.parameters},{self.block})"
    
    def LLVMDeclaration(self, module):
        functionType = ir.FunctionType(self.type.toLLVM(), [param.type.toLLVM() for param in self.parameters])
        function = ir.Function(module, functionType, name=self.name.value)
        self.function = function
        return function

    def allocaAndStore(self, builder, argument): 
        ptr = builder.alloca(argument.type)
        builder.store(argument, ptr)
        return ptr

    def toLLVM(self, module):
        block = self.function.append_basic_block()
        builder = ir.IRBuilder(block)
        param2var = {p.name.value:(self.allocaAndStore(builder, a),p.type) for p,a in zip(self.parameters, self.function.args)}
        builder.name2var = {**module.global2var, **param2var}
        self.block.toLLVM(builder)

class Block:
    def __init__(self, *args):
        self.statements = args
    def __str__(self):
        self.stmtsstr = ",".join([str(stmt) for stmt in self.statements])
        return f"Block({self.stmtsstr})"
    def toLLVM(self, builder):
        for stmt in self.statements: 
            stmt.toLLVM(builder)

class GlobalAssignement:
    def __init__(self, type, name, expr):
        self.type, self.name, self.expr = type, name, expr
    def __str__(self): 
        return f"GlobalAssignement({self.type},{self.name},{self.expr})"
    def LLVMDeclaration(self, module):
        gvar = ir.GlobalVariable(module, self.type.toLLVM(), self.name.value)
        gvar.linkage = "internal"
        self.reference = gvar
        return gvar
 
    def toLLVM(self, module):
        # function initializer
        functionType = ir.FunctionType(self.type.toLLVM(), [])
        function = ir.Function(module, functionType, name=f"0initilizer.{self.name.value}")
        function.reference = self.reference.gep([ir.Constant(ir.IntType(64), 0)])

        block = function.append_basic_block("entry")
        builder = ir.IRBuilder(block)
        builder.name2var = module.global2var
        builder.ret(self.expr.toLLVM(builder))

        return self.reference



class SlangTransformer(Transformer):


    # MODULEWISE DECLARATION
    def start                    (self, node): return Module(node)
    def slang_function           (self, node): return Function(node[1], node[2], node[3], node[5])
    def slang_parameter          (self, node): return Parameter(node[0], node[1])
    def slang_parameter_sequence (self, node): return ParameterSequence(*[param for param in node if isinstance(param,Parameter)])
    def slang_block              (self, node): return Block(*node)
    def slang_global_assignement (self, node): return GlobalAssignement(node[1].type, node[1].name, node[1].expr)

    # STATEMENTS
    def slang_return                 (self, node): return Return(node[1])
    def slang_declaration_assignment (self, node): return DeclareAssign(node[0], node[1], node[3])
    def slang_assignement            (self, node): return ReAssign(node[0], node[2])
    def slang_ifthen                 (self, node): return IfThen(node[1], node[3])
    def slang_while                  (self, node): return While(node[1], node[3])
    def slang_statement              (self, node): return node[0]
    def slang_skip                   (self,    _): return Skip();

    # EXPRESSIONS
    def slang_addition                       (self, node): return Add(node[0], node[2])
    def slang_subtraction                    (self, node): return Sub(node[0], node[2])
    def slang_multiplication                 (self, node): return Mul(node[0], node[2])
    def slang_division                       (self, node): return Div(node[0], node[2])
    def slang_modulo                         (self, node): return Mod(node[0], node[2])
    def slang_equality                       (self, node): return Eqs(node[0], node[2])
    def slang_greater                        (self, node): return Gtr(node[0], node[2])
    def slang_greaterEqual                   (self, node): return Gte(node[0], node[2])
    def slang_less                           (self, node): return Lss(node[0], node[2])
    def slang_lessEqual                      (self, node): return Lse(node[0], node[2])
    def slang_not_equal                      (self, node): return Neq(node[0], node[2])
    def slang_negative                       (self, node): return Neg(node[1])
    def slang_cast                           (self, node): return Cast(node[0], node[2])
    def slang_round_parenthesized            (self, node): return node[1]
    def slang_reference                      (self, node): return Ref(node[1])
    def slang_square_parenthesized           (self, node): return ValIndex(node[1])
    def slang_reference_square_parenthesized (self, node): return RefIndex(node[1])
    def slang_indexed                        (self, node): return Index(node[0], node[1:])
    def slang_array                          (self, node): return Array([child for child in node if isinstance(child, Expression)])
    def slang_expression_sequence            (self, node): return [n for n in node if isinstance(n, Expression)]
    def slang_function_call                  (self, node): return FunctionCall(node[0], node[2])

    # LITERALS
    def slang_identifier (self, node): return Name(node[0].value.strip())
    def slang_integer    (self, node): return Integer(node[0].value)
    def slang_rational   (self, node): return Rational(node[0].value)
    def slang_string     (self, node): return String(node[0].value)

    # NATIVE TYPES
    def slang_int64  (self, _): return Int64()
    def slang_int32  (self, _): return Int32()
    def slang_int8   (self, _): return Int8()
    def slang_double (self, _): return Double()
    def slang_pointer(self, node): return Pointer(node[0])


def parsed(programstr):
    res = lang.parse(programstr)
    return res

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
    binding.load_library_permanently(find_library('c'))

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
    rtype = [func.type for func in program.globals if func.name.value == "start"][-1]
    if rtype == Double(): cfunc = CFUNCTYPE(c_double)(func_ptr)
    if rtype == Int64(): cfunc = CFUNCTYPE(c_int64)(func_ptr)
    res = cfunc()
    return res

