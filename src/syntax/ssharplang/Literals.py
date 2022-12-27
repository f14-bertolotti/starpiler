from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

natural    = P(name = "ssharplang_natural"    , rules = [R(T("(0|[1-9]\d*)", regex=True))])
decimal    = P(name = "ssharplang_decimal"    , rules = [R(T("(0|[1-9]\d*)?\.\d+", regex=True))])
integer    = P(name = "ssharplang_integer"    , rules = [R(T("[+-]?"+natural.rules[0].rule[0].value, regex=True))])
rational   = P(name = "ssharplang_rational"   , rules = [R(T("[+-]?"+decimal.rules[0].rule[0].value, regex=True))])
identifier = P(name = "ssharplang_identifier" , rules = [R(T("[a-z_A-Z]\w*", regex=True))])
string     = P(name = "ssharplang_string"     , rules = [R(T("\"(?:[^\"]|\\.)*\"", regex=True))])

