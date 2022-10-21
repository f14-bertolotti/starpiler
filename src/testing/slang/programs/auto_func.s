
def int64 increment(int64 x) does return x + 1;;
def int64 apply(int8* f, int64 value) does return (f as (int64 -> int64)*)(value);;
def int64 start() does 
    auto f = &increment;
    return &apply(f as int8*, 10);
;
