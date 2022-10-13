from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import identifier, expression, native

statement              = P(name="slang_statement"              , mod="?")
block                  = P(name="slang_block"                  , rules = [R(statement, mod="*")])
skip                   = P(name="slang_skip"                   , rules = [R(T("skip"), T(";"))])
returnstmt             = P(name="slang_return"                 , rules = [R(T("return"), expression, T(";"))])
returnvoidstmt         = P(name="slang_return_void"            , rules = [R(T("return"), T(";"))])
declarationAssignement = P(name="slang_declaration_assignment" , rules = [R(native, identifier, T("="), expression, T(";"))])
autoAssignement        = P(name="slang_auto_assignement"       , rules = [R(T("auto"), identifier, T("="), expression, T(";"))])
assignement            = P(name="slang_assignement"            , rules = [R(expression, T("="), expression, T(";"))])
whileloop              = P(name="slang_while"                  , rules = [R(T("while"), expression, T("do"), block, T(";"))])
ifthen                 = P(name="slang_ifthen"                 , rules = [R(T("if"), expression, T("do"), block, T(";"))])
globalAssignement      = P(name="slang_global_assignement"     , rules = [R(T("def"), declarationAssignement)])
globalDeclaration      = P(name="slang_global_declaration"     , rules = [R(T("def"), native, identifier, T(";"))])
statement.append(ifthen, whileloop, declarationAssignement, autoAssignement, assignement, returnstmt, returnvoidstmt, skip, R(expression, T(";")))



