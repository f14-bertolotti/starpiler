
struct X with
    int64 x;
    int64 y;
    int64 z;
;

def int8* malloc(int64);
def void free(int8*);

def int64 start() does
    X* x = &malloc(size of X) as X*;
    &free(x as int8*);
    return 1;
;

