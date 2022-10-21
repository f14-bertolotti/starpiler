
def int64 x = 0;
def int64 y = 1;
def int64* z = [x + y,2,3,4];
def int64 start() does
    int64 result = x == 0 * y == 1 * 
             z[0] == 1 *
             z[1] == 2 *
             z[2] == 3 *
             z[3] == 4;
    return result;
;
