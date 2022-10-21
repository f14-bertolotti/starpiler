
def int64 start() does
    int64* x = [1,2];
    int64** y = [x,x];
    return x[0] == 1 * 
           x[1] == 2 *
           y[0][0] == 1 *
           y[0][1] == 2 *
           y[1][0] == 1 *
           y[1][1] == 2;
;
