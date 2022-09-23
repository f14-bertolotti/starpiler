from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import expr, ntype, identifier

statement = P(name="s_statement", mod="?")
block = P(name="s_block", rules = [R(statement, mod="*")])
skip = P(name="s_skip", rules=[R(T("skip"), T(";"))])
returnstmt = P(name="s_return", rules=[R(T("return"), expr, T(";"))])
assignement = P(name="s_assign", rules=[R(ntype, identifier, T("="), expr, T(";"))])
whileloop = P(name="s_while", rules=[R(T("while"), expr, T("do"), block, T(";"))])
statement.append(assignement, whileloop, returnstmt, skip)


