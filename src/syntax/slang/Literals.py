from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

natural    = P(name = "slang_natural"    , rules = [R(T("(0|[1-9]\d*)", regex=True))])
decimal    = P(name = "slang_decimal"    , rules = [R(T("(0|[1-9]\d*)?\.\d+", regex=True))])
integer    = P(name = "slang_integer"    , rules = [R(T("[+-]?"+natural.rules[0].rule[0].value, regex=True))])
rational   = P(name = "slang_rational"   , rules = [R(T("[+-]?"+decimal.rules[0].rule[0].value, regex=True))])
identifier = P(name = "slang_identifier" , rules = [R(T("(?!auto|return|if|while)[a-zA-Z]\w*", regex=True))]) 
string     = P(name = "slang_string"     , rules = [R(T("\"(?:[^\"\\\]|\\.)*\"", regex=True))])

