from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import native, identifier, block

parameter         = P(name = "slang_parameter"         , rules = [R(native, identifier)])
parameterSequence = P(name = "slang_parameter_sequence" , rules = [R(T("("), parameter, R(T(","), parameter, mod="*"), T(")")), R(T("("), T(")"))])
function          = P(name = "slang_function"          , rules = [R(T("def"), native, identifier, parameterSequence, T("does"), block, T(";"))])

