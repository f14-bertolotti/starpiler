
def int8* malloc(int64);
def void free(int8*);
def int8* memcpy(int8*,int8*,int32); 

def int64 start() does
    int64* x = [1,2,3,4,5];
    int64* y = &malloc(8 * 5) as int64*;
    &memcpy(y as int8*, x as int8*, (8 * 5) as int32);
    int64 result = y[0] == 1 * 
                   y[1] == 2 *
                   y[2] == 3 *
                   y[3] == 4 *
                   y[4] == 5;
    &free(y as int8*);
    return result;
;
