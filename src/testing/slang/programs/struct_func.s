
struct X with
    (int64 -> int64)* inc;
;

def int64 inc(int64 x) does return x + 1;;

def int64 start() does
    X* x = X{};
    x&.inc = &inc;
    return 0;; 

