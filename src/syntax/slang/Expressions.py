from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import rational, integer, identifier

expr = P(name = "s_expr", mod="?")
add = P(name = "s_add", rules=[R(expr, T("+"), expr)]) 
sub = P(name = "s_sub", rules=[R(expr, T("-"), expr)])
mul = P(name = "s_mul", rules=[R(expr, T("*"), expr)]) 
div = P(name = "s_div", rules=[R(expr, T("/"), expr)])
eql = P(name = "s_eql", rules=[R(expr, T("=="), expr)])
neq = P(name = "s_neq", rules=[R(expr, T("!="), expr)])
cld = P(name = "s_cld", rules=[R(T("("), expr, T(")"))])
fcl = P(name = "s_fcl", rules=[R(identifier, T("("), R(expr,mod="*"), T(")"))])
expr.append(add, sub, mul, div, neq, eql, rational, integer, identifier, cld, fcl)

