from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import identifier, expression, struct_name, native

statement              = P(name="slang_statement"              , mod="?")
block                  = P(name="slang_block"                  , rules = [R(statement, mod="*")])
skip                   = P(name="slang_skip"                   , rules = [R(T("skip"), T(";"))])
returnstmt             = P(name="slang_return"                 , rules = [R(T("return"), expression, T(";"))])
returnvoidstmt         = P(name="slang_return_void"            , rules = [R(T("return"), T(";"))])
declarationAssignement = P(name="slang_declaration_assignment" , rules = [R(native, identifier, T("="), expression)])
autoAssignement        = P(name="slang_auto_assignement"       , rules = [R(T("auto"), identifier, T("="), expression)])
assignement            = P(name="slang_assignement"            , rules = [R(expression, T("="), expression)])
whileloop              = P(name="slang_while"                  , rules = [R(T("while"), expression, T("do"), block, T(";"))])
ifthen                 = P(name="slang_ifthen"                 , rules = [R(T("if"), expression, T("do"), block, T(";"))])
globalAssignement      = P(name="slang_global_assignement"     , rules = [R(T("def"), declarationAssignement, T(";")), 
                                                                          R(T("def"), autoAssignement, T(";"))])
globalDeclaration      = P(name="slang_global_declaration"     , rules = [R(T("def"), native, identifier, T(";"))])

structDeclaration = P(name = "slang_struct_declaration"    , rules = [R(native, identifier, T(";"))])
structDefinition  = P(name = "slang_struct_definition"     , rules = [R(native, identifier, T("="), expression, T(";"))])
struct_name.append(structDeclaration, structDefinition)


expression.insert(0, assignement)
expression.insert(0, declarationAssignement)
expression.insert(0, autoAssignement)

statement.append(ifthen, 
                 whileloop, 
                 returnstmt, 
                 returnvoidstmt, 
                 skip, 
                 R(expression, T(";")))



