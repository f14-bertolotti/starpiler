
def int64 increment(int64 x) does
    return x + 1;
;

def int64 start() does
    int8* f = &increment as int8*;
    return (f as (int64 -> int64)*)(0);
;
