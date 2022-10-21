
struct X with 
        int64 x = 12;
        int64 y = x + 12;
;

def int64 start() does
        return X{}.x == 12 * X{}.y == 24;
;
