from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import rational, integer, identifier
from src.syntax.slang import ntype

expr = P(name = "s_expr", mod="?")
add = P(name = "s_add", rules=[R(expr, T("+"), expr)]) 
sub = P(name = "s_sub", rules=[R(expr, T("-"), expr)])
mul = P(name = "s_mul", rules=[R(expr, T("*"), expr)]) 
div = P(name = "s_div", rules=[R(expr, T("/"), expr)])
mod = P(name = "s_mod", rules=[R(expr, T("%"), expr)])
neg = P(name = "s_neg", rules=[R(T("-"), expr)])
eql = P(name = "s_eql", rules=[R(expr, T("=="), expr)])
gtr = P(name = "s_gtr", rules=[R(expr, T(">") , expr)])
gte = P(name = "s_gte", rules=[R(expr, T(">="), expr)])
lss = P(name = "s_lss", rules=[R(expr, T("<") , expr)])
lse = P(name = "s_lse", rules=[R(expr, T("<="), expr)])
neq = P(name = "s_neq", rules=[R(expr, T("!="), expr)])
cld = P(name = "s_cld", rules=[R(T("("), expr, T(")"))])
sqt = P(name = "s_sqt", rules=[R(T("["), expr, T("]"), mod="+")])
idx = P(name = "s_idx", rules=[R(expr, sqt)])
esq = P(name = "s_esq", rules=[expr, R(expr, T(","), R(expr,mod="*"))])
fcl = P(name = "s_fcl", rules=[R(identifier, T("("), esq, T(")"))])
cst = P(name = "s_cst", rules=[R(T("("), ntype, T(")"), expr)])
expr.append(add, sub, mul, div, mod, neq, eql, gtr, gte, lss, lse, neg, rational, integer, identifier, cld, fcl, cst, idx)

