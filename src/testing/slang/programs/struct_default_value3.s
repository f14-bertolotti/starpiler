
def int64 x = 8;
def int64 z = 12 + x;
struct X with 
        int64 x = 12;
        int64 y = x + 12;
        int64 z = z + y;
        int64 w = z;
;

def int64 start() does
        return X{}.x == 12 * 
               X{}.y == 24 * 
               X{}.z == 44 *
               X{}.w == 44 *
               z == 20 * 
               x == 8;
;
