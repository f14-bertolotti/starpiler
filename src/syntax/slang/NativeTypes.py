from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

int64   = P(name = "slang_int64"  , rules = [R(T("int64"))])
int32   = P(name = "slang_int32"  , rules = [R(T("int32"))])
int8    = P(name = "slang_int8"   , rules = [R(T("int8"))])
double  = P(name = "slang_double" , rules = [R(T("double"))])
native  = P(name = "slang_type"   , rules = [double, int64, int32, int8], mod="?")
pointer = P(name = "slang_pointer", rules = [R(native, T("*"))])
native.append(pointer)
