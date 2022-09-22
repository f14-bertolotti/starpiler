from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import ntype, identifier, statement

parameter = P(name = "s_param", rules = [R(ntype, identifier)])
function = P(name = "s_func", rules = [R(T("def"), ntype, identifier, T("("), R(parameter, mod="*"), T(")"), T("does"), R(statement,mod="*"), T(";"))])

