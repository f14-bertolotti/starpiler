from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.slang import identifier

int64   = P(name = "slang_int64"  , rules = [R(T("int64"))])
int32   = P(name = "slang_int32"  , rules = [R(T("int32"))])
int8    = P(name = "slang_int8"   , rules = [R(T("int8"))])
double  = P(name = "slang_double" , rules = [R(T("double"))])
void    = P(name = "slang_void"   , rules = [R(T("void"))])
custom  = P(name = "slang_tname"  , rules = [identifier])
native  = P(name = "slang_type"   , rules = [double, int64, int32, int8, void, custom], mod="?")
pointer = P(name = "slang_pointer", rules = [R(native, T("*"))])
ptype   = P(name = "slang_ptype"  , rules = [R(T("(")), 
                                             R(T("("), native, R(T(","), native, mod="*"))])
struct  = P(name = "slang_struct" , rules = [R(T("struct"), identifier, T("with"), R(native, identifier, T(";"), mod="*"), T(";"))])
rtype   = P(name = "slang_rtype"  , rules = [R(T("->"), native, T(")"))])
ftype   = P(name = "slang_ftype"  , rules = [R(ptype, rtype)])
native.append(pointer,ftype)
