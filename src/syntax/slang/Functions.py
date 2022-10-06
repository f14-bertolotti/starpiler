from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import native, identifier, block

varargParameter     = P(name = "slang_vararg_parameter"     , rules = [T("...")])
parameterDefinition = P(name = "slang_parameter_definition" , rules = [R(native, identifier)])
parameterDeclaration= P(name = "slang_parameter_declaration", rules = [R(native), R(varargParameter)])
parameterSeqDef     = P(name = "slang_parameter_seq_def"    , rules = [R(T("("), parameterDefinition, R(T(","), parameterDefinition, mod="*"), T(")")), R(T("("), T(")"))])
parameterSeqDecl    = P(name = "slang_parameter_seq_decl"   , rules = [R(T("("), parameterDeclaration, R(T(","), parameterDeclaration, mod="*"), T(")")), R(T("("), T(")"))])
functionDeclaration = P(name = "slang_function_declaration" , rules = [R(T("def"), native, identifier, parameterSeqDecl, T(";"))])
functionDefinition  = P(name = "slang_function_definition"  , rules = [R(T("def"), native, identifier, parameterSeqDef , T("does"), block, T(";"))])

