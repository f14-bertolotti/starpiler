from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.ssharplang import native, identifier, block

varargParameter     = P(name = "ssharplang_vararg_parameter"     , rules = [T("...")])
parameterDefinition = P(name = "ssharplang_parameter_definition" , rules = [R(native, identifier)])
parameterDeclaration= P(name = "ssharplang_parameter_declaration", rules = [R(native), R(varargParameter)])
parameterSeqDef     = P(name = "ssharplang_parameter_seq_def"    , rules = [R(T("("), parameterDefinition, R(T(","), parameterDefinition, mod="*"), T(")")), R(T("("), T(")"))])
parameterSeqDecl    = P(name = "ssharplang_parameter_seq_decl"   , rules = [R(T("("), parameterDeclaration, R(T(","), parameterDeclaration, mod="*"), T(")")), R(T("("), T(")"))])
functionDeclaration = P(name = "ssharplang_function_declaration" , rules = [R(T("fun"), native, identifier, parameterSeqDecl)])
functionDefinition  = P(name = "ssharplang_function_definition"  , rules = [R(T("fun"), native, identifier, parameterSeqDef , T("{"), block, T("}"))])

