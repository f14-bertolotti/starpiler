
struct XY with int64 x; int64 y; XY* xy;;

def int64 start() does
    auto y = XY{x:1, y:2, xy:XY{x:1, y:2, xy:0 as XY*}};
    return y.xy.y;
;
