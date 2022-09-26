from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import expr, ntype, identifier

statement = P(name="s_statement", mod="?")
block = P(name="s_block", rules = [R(statement, mod="*")])
skip = P(name="s_skip", rules=[R(T("skip"), T(";"))])
returnstmt = P(name="s_return", rules=[R(T("return"), expr, T(";"))])
declare_assign = P(name="s_decl_assign", rules=[R(ntype, identifier, T("="), expr, T(";"))])
nodeclr_assign = P(name="s_nodecl_assign", rules=[R(identifier, T("="), expr, T(";"))])
assignement = P(name="s_assign", rules=[declare_assign, nodeclr_assign], mod="?")
whileloop = P(name="s_while", rules=[R(T("while"), expr, T("do"), block, T(";"))])
ifthen = P(name="s_ifthen", rules=[R(T("if"), expr, T("do"), block, T(";"))])
statement.append(ifthen, whileloop, assignement, returnstmt, skip)


