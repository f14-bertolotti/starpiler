from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.ssharplang import identifier, block, native, ftype

fieldDefinition    = P(name = "ssharplang_field_definition"   , rules = [R(T("var"), native, identifier, T(";"))])

identifierSequence = P(name = "ssharplang_identifier_sequence", rules = [R(T("("),T(")")), R(T("("), identifier, R(T(","), identifier, mod="*"), T(")"))])
methodDefinition   = P(name = "ssharplang_method_definition"  , rules = [R(T("fun"), ftype, identifier, identifierSequence, T("{"), block, T("}"))])


fieldSequence      = P(name = "ssharplang_field_sequence"     , rules = [fieldDefinition, methodDefinition], mod="?")
classDefinition    = P(name = "ssharplang_class_definition"   , rules = [R(T("class"), identifier, T("{"), R(fieldSequence, mod="*"), T("}"))])

