
struct XY with int64 x; int64 y; XY* xy;;

def int64 start() does 
    auto x = XY{x:0, y:1, xy:0 as XY*};
    return x.y;
;
