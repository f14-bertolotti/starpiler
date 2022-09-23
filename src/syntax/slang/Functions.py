from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import ntype, identifier, block

parameter = P(name = "s_param", rules = [R(ntype, identifier)])
parameters = P(name = "s_param_seq", rules=[R(T("("), R(parameter, T(","), mod="*"), parameter, T(")")), 
                                            R(T("("), T(")"))])
function = P(name = "s_func", rules = [R(T("def"), ntype, identifier, parameters, T("does"), block, T(";"))])

