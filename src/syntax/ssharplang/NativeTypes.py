from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.ssharplang import identifier


int64   = P(name = "ssharplang_int64"  , rules = [R(T("int64"))])
int32   = P(name = "ssharplang_int32"  , rules = [R(T("int32"))])
int8    = P(name = "ssharplang_int8"   , rules = [R(T("int8"))])
double  = P(name = "ssharplang_double" , rules = [R(T("double"))])
void    = P(name = "ssharplang_void"   , rules = [R(T("void"))])
custom  = P(name = "ssharplang_tname"  , rules = [identifier])
native  = P(name = "ssharplang_type"   , rules = [double, int64, int32, int8, void, custom], mod="?")
ptype   = P(name = "ssharplang_ptype"  , rules = [R(T("(")), R(T("("), native, R(T(","), native, mod="*"))])
rtype   = P(name = "ssharplang_rtype"  , rules = [R(T("->"), native, T(")"))])
ftype   = P(name = "ssharplang_ftype"  , rules = [R(ptype, rtype)])
atype   = P(name = "ssharplang_atype"  , rules = [R(native, T("["), T("]"))])
native.append(ftype)
native.append(atype)
