
def int8* malloc(int64);
def void free(int8*);

def int64 start() does
    int64* x = &malloc(8 * 3) as int64*;
    x&[0] = 0;
    x&[1] = 0;
    x&[2] = 0;
    int64 a = x[0];
    int64 b = x[1];
    int64 c = x[2];
    &free(x as int8*);
    return a == b * b == c * c == 0;
;
