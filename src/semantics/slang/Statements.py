from src.semantics.slang import Void, Int8, Int32, Int64, Double, Pointer
from llvmlite import ir
import copy

class DeclareAssign:
    def __init__(self, type, name, expr):
        self.type, self.name, self.expr = type, name, expr
    def __str__(self):
        return f"Ass({self.type},{self.name},{self.expr})"
    def toLLVM(self, builder):
        expr = self.expr.toLLVM(builder)
        self.ref = builder.alloca(self.type.toLLVM())

        builder.store(expr, self.ref)
        builder.name2var[self.name.value] = self

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
        cond = builder.icmp_signed("==",self.cond.toLLVM(builder), ir.Constant(ir.IntType(64), 1))

        builder.name2var, tmp = copy.deepcopy(builder.name2var), builder.name2var
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
    
        cond = whilebuilder.icmp_signed("==", self.cond.toLLVM(whilebuilder), ir.Constant(ir.IntType(64), 1))
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
        builder.ret(self.expr.toLLVM(builder))

