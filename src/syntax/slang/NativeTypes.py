from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

int64   = P(name = "s_int64"  , rules = [R(T("int64"))])
float64 = P(name = "s_float64", rules = [R(T("float64"))])
ntype   = P(name = "s_type"   , rules = [int64, float64])
