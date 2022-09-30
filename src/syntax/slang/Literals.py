from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

natural    = P(name = "s_natural"    , rules = [R(T("(0|[1-9]\d*)", regex=True))])
decimal    = P(name = "s_decimal"    , rules = [R(T("(0|[1-9]\d*)?\.\d+", regex=True))])
integer    = P(name = "s_integer"    , rules = [R(T("[+-]?"+natural.rules[0].rule[0].value, regex=True))])
rational   = P(name = "s_rational"   , rules = [R(T("[+-]?"+decimal.rules[0].rule[0].value, regex=True))])
identifier = P(name = "s_identifier" , rules = [R(T("(?!return|if|while)[a-zA-Z]\w*", regex=True))]) 
string     = P(name = "s_string"     , rules = [R(T("\"(?:[^\"\\\]|\\.)*\"", regex=True))])
arrayValue = P(name = "s_array_value", rules = [integer, rational, string], mod="?")
array      = P(name = "s_array"      , rules = [R(T("["), T("]")), R(T("["), arrayValue, R(T(","), arrayValue, mod="*"), T("]"))])
arrayValue.append(array)
