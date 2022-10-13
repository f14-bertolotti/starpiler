from src.syntax.slang import lang

from llvmlite import ir
from llvmlite import binding 
from lark.visitors import Transformer
from lark.lexer import Token

from ctypes import CFUNCTYPE, c_double, c_int64
from ctypes.util import find_library

from src.semantics.slang import *
import os, pathlib

class Module:
    def __init__(self, declarations):
        self.LLVMModule = ir.Module()
        self.declarations = declarations
        self.LLVMModule.name2decl = dict()
        self.LLVMModule.path2import = dict()
        self.LLVMModule.compiled = set()
        
    def __str__(self):
        string = ",".join([str(gbl) for gbl in self.declarations])
        return f"Module({string})"

    def toLLVM(self):

        self.LLVMModule.path2import[pathlib.Path()] = self.LLVMModule.name2decl

        for dcl in self.declarations:
            dcl.LLVMDeclare(self.LLVMModule)

        self.LLVMModule.name2decl["start"].globalsBuilder = ir.IRBuilder(self.LLVMModule.name2decl["start"].ref.append_basic_block())

        for dcl in self.declarations:
            dcl.toLLVM(self.LLVMModule)

        self.LLVMModule.name2decl["start"].globalsBuilder.branch(self.LLVMModule.name2decl["start"].block.ref)

        return self.LLVMModule

class VarArgParameter:
    def __init__(self): pass

class ParameterDeclaration:
    def __init__(self, type):
        self.type = type
    def getType(self):
        return self.type

class ParameterDefinition:
    def __init__(self, type, name):
        self.type, self.name = type, name
    def __str__(self):
        return f"Parameter({self.type},{self.name})"
    def getType(self):
        return self.type
    def toLLVM(self, builder, llvmParam):
        self.ref = builder.alloca(llvmParam.type)
        builder.store(llvmParam, self.ref)
        builder.name2var[self.name.value] = self

class ParameterSequenceDeclaration:
    def __init__(self, *args):
        self.parameters = args
    def isVariable(self):
        return any([isinstance(p.getType(), VarArgParameter) for p in self.parameters])
    def getType(self):
        return [p.getType() for p in self.parameters if not isinstance(p.type, VarArgParameter)]
    def toLLVM(self):
        pass

class ParameterSequenceDefinition:
    def __init__(self, *args):
        self.parameters = args
    def __str__(self):
        paramsstr = ",".join(str(param) for param in self.parameters)
        return f"ParamSeqDef({paramsstr})"
    def getType(self):
        return [p.getType() for p in self.parameters]
    def toLLVM(self, builder, llvmParameters):
        for myParam, llvmParam in zip(self.parameters, llvmParameters):
            myParam.toLLVM(builder, llvmParam)

class FunctionDefinition:
    def __init__(self, rtype, name, parameters, block):
        self.type = FType(parameters.getType(), rtype)
        self.parameters = parameters
        self.block = block
        self.name = name
        self.ref = None
    
    def __str__(self):
        return f"FunctionDefinition({self.name},{self.parameters},{self.block})"

    def LLVMDeclare(self, module):
        self.ref = ir.Function(module, self.type.toLLVM(module), name=self.name.value)
        module.name2decl[self.name.value] = self

    def toLLVM(self, module):
        basicBlock = self.ref.append_basic_block()
        builder = ir.IRBuilder(basicBlock)
        builder.name2var = {**module.name2decl}
        self.parameters.toLLVM(builder, self.ref.args)
        self.block.toLLVM(builder)

class FunctionDeclaration:
    def __init__(self, rtype, name, parameters): 
        self.type = FType(parameters.getType(), rtype, vararg=True) if parameters.isVariable() else FType(parameters.getType(), rtype)
        self.parameters = parameters
        self.name = name
        self.ref = None

    def __str__(self):
        return f"FunctionDeclaration({self.type},{self.name})"
        
    def LLVMDeclare(self, module):
        self.ref = ir.Function(module, self.type.toLLVM(module), name=self.name.value)
        module.name2decl[self.name.value] = self

    def toLLVM(self, module): pass


class GlobalAssignement:
    def __init__(self, type, name, expr):
        self.type, self.name, self.expr, self.ref = type, name, expr, None

    def __str__(self): 
        return f"GlobalAssignement({self.type},{self.name},{self.expr})"

    def LLVMDeclare(self, module):
        gvar = ir.GlobalVariable(module, self.type.toLLVM(module), self.name.value)
        self.ref = gvar
        module.name2decl[self.name.value] = self
        gvar.linkage = "internal"

    def toLLVM(self, module):
        builder = module.name2decl["start"].globalsBuilder
        builder.name2var = module.name2decl
        builder.store(self.expr.toLLVM(builder), self.ref)

class GlobalDeclaration:
    def __init__(self, type, name):
        self.type, self.name, self.ref = type, name, None

    def __str__(self): 
        return f"GlobalDeclaration({self.type},{self.name})"

    def LLVMDeclare(self, module):
        gvar = ir.GlobalVariable(module, self.type.toLLVM(module), self.name.value)
        self.ref = gvar
        module.name2decl[self.name.value] = self
        gvar.linkage = "internal"

    def toLLVM(self, module):
        pass
 

class Import:
    
    path2module = dict()
    compiled = set()
    def __init__(self, path, name, rename):
        self.path, self.name, self.rename = pathlib.Path(os.path.join(os.getcwd(), path)), name, rename
        
        if self.path in Import.path2module: self.module = Import.path2module[self.path]
        else:
            self.module = transformed(self.path.read_text(), self.path)
            Import.path2module[self.path] = self.module

    def __str__(self):
        return f"Import({self.path},{self.name},{self.rename})"

    def LLVMDeclare(self, module):
        if self.path not in module.path2import:
            module.name2decl, tmp = dict(), module.name2decl
            module.path2import[self.path] = module.name2decl

            for dcl in self.module.declarations:
                dcl.LLVMDeclare(module)

            module.name2decl = tmp

        module.name2decl[self.rename.value] = module.path2import[self.path][self.name.value]

    def toLLVM(self, module): 
        if self.path not in module.compiled:
            module.compiled.add(self.path)

            module.name2decl, tmp = module.path2import[self.path], module.name2decl
            module.name2decl["start"] = tmp["start"]
            for dcl in self.module.declarations:
                dcl.toLLVM(module)
            module.name2decl = tmp

class StructDeclaration:
    def __init__(self, name, names, types): 
        self.name, self.types, self.names, self.type = name, types, names, SType(name)
    def __str__(self): 
        typesstr = ",".join([f"{n}:{t}" for n,t in zip(self.names, self.types)]) 
        return f"StructDecl({self.name},{typesstr})"
    def LLVMDeclare(self,module):
        self.ref = ir.global_context.get_identified_type(f"struct.{self.name.value}")
        module.name2decl[self.name.value] = self
        self.ref.set_body(*[t.toLLVM(module) for t in self.types])
    def toLLVM(self, module):
        pass

class Block:
    def __init__(self, *args):
        self.statements, self.ref = args, None
    def __str__(self):
        self.stmtsstr = ",".join([str(stmt) for stmt in self.statements])
        return f"Block({self.stmtsstr})"
    def toLLVM(self, builder):
        self.ref = builder.basic_block
        for stmt in self.statements: 
            stmt.toLLVM(builder)


class SlangTransformer(Transformer):

    def __init__(self, *args, path=pathlib.Path(), **kwargs):
        super().__init__(self, *args, **kwargs)
        self.path = path

    # MODULEWISE DECLARATION
    def slang_start                (self, node): return Module(node)
    def slang_vararg_parameter     (self, node): return VarArgParameter()
    def slang_parameter_definition (self, node): return ParameterDefinition(node[0], node[1])
    def slang_parameter_declaration(self, node): return ParameterDeclaration(node[0])
    def slang_parameter_seq_def    (self, node): return ParameterSequenceDefinition (*[param for param in node if isinstance(param,ParameterDefinition )])
    def slang_parameter_seq_decl   (self, node): return ParameterSequenceDeclaration(*[param for param in node if isinstance(param,ParameterDeclaration)])
    def slang_block                (self, node): return Block(*node)
    def slang_global_assignement   (self, node): return GlobalAssignement(node[1].type, node[1].name, node[1].expr)
    def slang_global_declaration   (self, node): return GlobalDeclaration(node[1], node[2])
    def slang_import               (self, node): return Import(node[1].value[:-1], node[3], node[5])
    def slang_function_definition  (self, node): return FunctionDefinition(node[1], node[2], node[3], node[5])
    def slang_function_declaration (self, node): return FunctionDeclaration(node[1], node[2], node[3])

    # STATEMENTS
    def slang_return                 (self, node): return Return(node[1])
    def slang_return_void            (self, node): return ReturnVoid()
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
    def slang_greater_equal                  (self, node): return Gte(node[0], node[2])
    def slang_less                           (self, node): return Lss(node[0], node[2])
    def slang_less_equal                     (self, node): return Lse(node[0], node[2])
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
    def slang_struct_value                   (self, node): return StructValue(node[0], node[2:-1:4], node[4:-1:4])
    def slang_struct_access                  (self, node): return StructAccess(node[0], node[2])
    def slang_struct_ref_access              (self, node): return StructRefAccess(node[0], node[2])

    # LITERALS
    def slang_identifier (self, node): return Name(node[0].value.strip())
    def slang_integer    (self, node): return Integer(node[0].value)
    def slang_rational   (self, node): return Rational(node[0].value)
    def slang_string     (self, node): return String(node[0].value)
    def slang_tname      (self, node): return SType(node[0], path=self.path)

    # NATIVE TYPES
    def slang_int64  (self, _): return Int64()
    def slang_int32  (self, _): return Int32()
    def slang_int8   (self, _): return Int8()
    def slang_void   (self, _): return Void()
    def slang_double (self, _): return Double()
    def slang_pointer(self, node): return Pointer(node[0])
    def slang_ptype  (self, node): return node[1:]
    def slang_rtype  (self, node): return node[1]
    def slang_ftype  (self, node): return FType(node[0], node[1])
    def slang_struct (self, node): return StructDeclaration(node[1], node[4:-1:3], node[3:-1:3])


def parsed(programstr):
    res = lang.parse(programstr)
    return res

def transformed(programstr, path=pathlib.Path()):
    return SlangTransformer(path=path).transform(parsed(programstr))

def assembled(programstr):
    return str(transformed(programstr).toLLVM())

def run(programstr):
    # This shitty code resets the context 
    # since there is no other documented way for doing so
    # probably will brake shit about fuck
    ir.global_context.scope = ir._utils.NameScope()  
    ir.global_context.identified_types.clear()      


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

    rtype = module.name2decl["start"].type.rtype

    if rtype == Double(): cfunc = CFUNCTYPE(c_double)(func_ptr)
    if rtype == Int64(): cfunc = CFUNCTYPE(c_int64)(func_ptr)
    res = cfunc()
    return res

