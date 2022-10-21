
def int32 printf(int8*, ...);
def int8* malloc(int64);
def void free(int8*);

def int64 start() does
    int8* f = &malloc(3) as int8*;
    int8* s = &malloc(1) as int8*;
    s&[0] = 65 as int8;
    s&[1] = 65 as int8;
    s&[2] = 0 as int8;
    f&[0] = 0 as int8;
    &printf(f,s);
    &free(f);
    &free(s);
    return 0;
;            
