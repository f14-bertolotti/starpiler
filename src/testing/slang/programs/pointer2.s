
def int8* malloc(int64);
def void free(int8*);

def int64 start() does
    int64** x = &malloc(8 * 3) as int64**;
    x&[0] = &malloc(8 * 3) as int64*;
    x&[1] = &malloc(8 * 3) as int64*;
    x&[2] = &malloc(8 * 3) as int64*;
    x[0]&[0] = 0;
    x[0]&[1] = 1;
    x[0]&[2] = 2;
    x[1]&[0] = 3;
    x[1]&[1] = 4;
    x[1]&[2] = 5;
    x[2]&[0] = 6;
    x[2]&[1] = 7;
    x[2]&[2] = 8;
    int64 result = x[0][0] == 0 * 
                   x[0][1] == 1 * 
                   x[0][2] == 2 *
                   x[1][0] == 3 *
                   x[1][1] == 4 *
                   x[1][2] == 5 *
                   x[2][0] == 6 *
                   x[2][1] == 7 *
                   x[2][2] == 8;

    &free(x[0] as int8*);
    &free(x[1] as int8*);
    &free(x[2] as int8*);
    &free(x as int8*);

    return result;
;
