from lark.visitors import Transformer

from src.semantics.whilelang.c import integer
from src.semantics.whilelang.c import identifier
from src.semantics.whilelang.c import addition
from src.semantics.whilelang.c import subtraction
from src.semantics.whilelang.c import multiplication
from src.semantics.whilelang.c import division
from src.semantics.whilelang.c import equality
from src.semantics.whilelang.c import inequality
from src.semantics.whilelang.c import concat
from src.semantics.whilelang.c import assignement
from src.semantics.whilelang.c import whileloop
from src.semantics.whilelang.c import ifcondition


def start(self, tree):
    return "int main() {" + tree[0].children[0] + "}"

Transpiler = type("Transpiler", (Transformer,), 
                {"int":integer, 
                 "id": identifier,
                 "add": addition,
                 "sub": subtraction,
                 "mul": multiplication,
                 "div": division,
                 "eq": equality,
                 "neq": inequality,
                 "cat": concat,
                 "assign":assignement,
                 "while":whileloop,
                 "if":ifcondition,
                 "start":start}) 
