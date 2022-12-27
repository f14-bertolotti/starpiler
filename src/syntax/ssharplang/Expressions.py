from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.ssharplang import native, rational, integer, identifier, string

expression = P(name = "ssharplang_expression", mod="?")


addition       = P(name = "ssharplang_addition"       , rules=[R(expression, T("+"), expression)])
subtraction    = P(name = "ssharplang_subtraction"    , rules=[R(expression, T("-"), expression)])
multiplication = P(name = "ssharplang_multiplication" , rules=[R(expression, T("*"), expression)])
division       = P(name = "ssharplang_division"       , rules=[R(expression, T("/"), expression)])
modulo         = P(name = "ssharplang_modulo"         , rules=[R(expression, T("%"), expression)])
negative       = P(name = "ssharplang_negative"       , rules=[R(T("-"), expression)])
equality       = P(name = "ssharplang_equality"       , rules=[R(expression, T("=="), expression)])
greater        = P(name = "ssharplang_greater"        , rules=[R(expression, T(">") , expression)])
greaterEqual   = P(name = "ssharplang_greater_equal"  , rules=[R(expression, T(">="), expression)])
less           = P(name = "ssharplang_less"           , rules=[R(expression, T("<") , expression)])
lessEqual      = P(name = "ssharplang_less_equal"     , rules=[R(expression, T("<="), expression)])
notEqual       = P(name = "ssharplang_not_equal"      , rules=[R(expression, T("!="), expression)])
reference      = P(name = "ssharplang_reference"      , rules=[R(T("&"), identifier)])
sizeOf         = P(name = "ssharplang_size_of"        , rules=[R(T("size"), T("of"), native)]) 

roundParenthesized           = P(name = "ssharplang_round_parenthesized"           , rules=[R(T("("), expression, T(")"))])
squareParenthesized          = P(name = "ssharplang_square_parenthesized"           , rules=[R(T("["), expression, T("]"))])
referenceSquareParenthesized = P(name = "ssharplang_reference_square_parenthesized" , rules=[R(T("&["), expression, T("]"))])
parenthesized                = P(name = "ssharplang_parenthesized"                , rules=[squareParenthesized, referenceSquareParenthesized], mod="?")
indexed                      = P(name = "ssharplang_indexed"                      , rules=[R(expression, R(parenthesized, mod="+"))])

expressionSequence = P(name = "ssharplang_expression_sequence" , rules=[expression, R(expression, R(T(","), expression, mod="*"))])
functionCall       = P(name = "ssharplang_function_call"       , rules=[R(expression, T("("), expressionSequence, T(")")), 
                                                                   R(expression, T("("),T(")"))])
cast               = P(name = "ssharplang_cast"               , rules=[R(expression, T("as"), native)])

structValue = P(name = "ssharplang_struct_value",  rules = [R(identifier, T("{"), identifier, T(":"), expression, R(T(","), identifier, T(":"), expression, mod="*"), T("}")),
                                                       R(identifier, T("{"), T("}"))])
structAccess    = P(name = "ssharplang_struct_access"    , rules = [R(expression, T("."), identifier)])
structRefAccess = P(name = "ssharplang_struct_ref_access", rules = [R(expression, T("&."),identifier)]) 

array = P(name = "ssharplang_array", rules = [R(T("["), T("]")), R(T("["), expression, R(T(","), expression, mod="*"), T("]"))])

expression.append(identifier,
                  addition, 
                  subtraction, 
                  multiplication, 
                  division, 
                  modulo, 
                  notEqual, 
                  equality, 
                  greater, 
                  greaterEqual, 
                  less, 
                  lessEqual, 
                  negative, 
                  rational, 
                  integer, 
                  string, 
                  array, 
                  functionCall, 
                  cast, 
                  reference, 
                  structValue,
                  structAccess,
                  structRefAccess,
                  indexed, 
                  sizeOf,
                  roundParenthesized) 

