from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import native, rational, integer, identifier, string

expression = P(name = "slang_expression", mod="?")


addition       = P(name = "slang_addition"       , rules=[R(expression, T("+"), expression)])
subtraction    = P(name = "slang_subtraction"    , rules=[R(expression, T("-"), expression)])
multiplication = P(name = "slang_multiplication" , rules=[R(expression, T("*"), expression)])
division       = P(name = "slang_division"       , rules=[R(expression, T("/"), expression)])
modulo         = P(name = "slang_modulo"         , rules=[R(expression, T("%"), expression)])
negative       = P(name = "slang_negative"       , rules=[R(T("-"), expression)])
equality       = P(name = "slang_equality"       , rules=[R(expression, T("=="), expression)])
greater        = P(name = "slang_greater"        , rules=[R(expression, T(">") , expression)])
greaterEqual   = P(name = "slang_greater_equal"  , rules=[R(expression, T(">="), expression)])
less           = P(name = "slang_less"           , rules=[R(expression, T("<") , expression)])
lessEqual      = P(name = "slang_less_equal"     , rules=[R(expression, T("<="), expression)])
notEqual       = P(name = "slang_not_equal"      , rules=[R(expression, T("!="), expression)])
reference      = P(name = "slang_reference"      , rules=[R(T("&"), identifier)])
sizeOf         = P(name = "slang_size_of"        , rules=[R(T("size"), T("of"), native)]) 

roundParenthesized           = P(name = "slang_round_parenthesized"           , rules=[R(T("("), expression, T(")"))])
squareParenthesized          = P(name = "slang_square_parenthesized"           , rules=[R(T("["), expression, T("]"))])
referenceSquareParenthesized = P(name = "slang_reference_square_parenthesized" , rules=[R(T("&["), expression, T("]"))])
parenthesized                = P(name = "slang_parenthesized"                , rules=[squareParenthesized, referenceSquareParenthesized], mod="?")
indexed                      = P(name = "slang_indexed"                      , rules=[R(expression, R(parenthesized, mod="+"))])

expressionSequence = P(name = "slang_expression_sequence" , rules=[expression, R(expression, R(T(","), expression, mod="*"))])
functionCall       = P(name = "slang_function_call"       , rules=[R(expression, T("("), expressionSequence, T(")")), R(expression, T("("),T(")"))])
cast               = P(name = "slang_cast"               , rules=[R(expression, T("as"), native)])

structValue = P(name = "slang_struct_value",  rules = [R(identifier, T("{"), identifier, T(":"), expression, R(T(","), identifier, T(":"), expression, mod="*"), T("}")),
                                                       R(identifier, T("{"), T("}"))])
structAccess    = P(name = "slang_struct_access"    , rules = [R(expression, T("."), identifier)])
structRefAccess = P(name = "slang_struct_ref_access", rules = [R(expression, T("&."),identifier)]) 

array = P(name = "slang_array", rules = [R(T("["), T("]")), R(T("["), expression, R(T(","), expression, mod="*"), T("]"))])

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

