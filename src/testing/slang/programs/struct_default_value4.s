
def int64 zero() does return 0;;
struct X with 
        ( -> int64)* zero = &zero;
;

def int64 start() does
        return X{}.zero() == 0; 
;
