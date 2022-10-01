from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

int64   = P(name = "s_int64"  , rules = [R(T("int64"))])
int32   = P(name = "s_int32"  , rules = [R(T("int32"))])
int8    = P(name = "s_int8"   , rules = [R(T("int8"))])
float64 = P(name = "s_float64", rules = [R(T("float64"))])
ntype   = P(name = "s_type"   , rules = [int64, int32, int8, float64], mod="?")
pttype  = P(name = "s_ptr"    , rules = [R(ntype, T("*"))])
ntype.append(pttype)
