from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.ssharplang import identifier, expression, native

statement              = P(name="ssharplang_statement"              , rules = [], mod="?")
block                  = P(name="ssharplang_block"                  , rules = [R(statement, mod="+")])
skip                   = P(name="ssharplang_skip"                   , rules = [R(T("skip"), T(";"))])
returnstmt             = P(name="ssharplang_return"                 , rules = [R(T("return"), expression, T(";"))])
returnvoidstmt         = P(name="ssharplang_return_void"            , rules = [R(T("return"), T(";"))])
whileloop              = P(name="ssharplang_while"                  , rules = [R(T("while"), T("("), expression, T(")"), T("{"), block, T("}"))])
ifthen                 = P(name="ssharplang_ifthen"                 , rules = [R(T("if"), T("("), expression, T(")"), T("{"), block, T("}"))])
stmtexpr               = P(name="ssharplang_stmt_expr"              , rules = [R(expression, T(";"))], mod="?")
forloop                = P(name="ssharplang_for"                    , rules = [R(T("for"), identifier, T("from"), expression, T("{"), block, T("}"))])

declarationAssignement = P(name="ssharplang_declaration_assignment" , rules = [R(native, identifier, T("="), expression, T(";"))])
autoAssignement        = P(name="ssharplang_auto_assignement"       , rules = [R(T("auto"), identifier, T("="), expression, T(";"))])
assignement            = P(name="ssharplang_assignement"            , rules = [R(expression, T("="), expression, T(";"))])

statement.append(ifthen, 
                 whileloop, 
                 forloop,
                 declarationAssignement,
                 autoAssignement,
                 assignement,
                 returnstmt, 
                 returnvoidstmt, 
                 skip,
                 stmtexpr)
                

