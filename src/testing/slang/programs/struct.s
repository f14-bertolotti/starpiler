
struct XY with
    int64 x;
    int8* y;
;

def int64 start() does
    XY* xy = XY{x:1, y:0 as int8*};
    return xy.x;
;
