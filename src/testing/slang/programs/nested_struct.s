
struct XY with
    int64 x;
    int64 y;
    XY*  xy;
;

def int64 start() does
    XY* xy = XY{x:1, y:1, xy:XY{x:2, y:2, xy:0 as XY*}};
    return xy.x == 1 *
           xy.y == 1 *
           xy.xy.x == 2 *
           xy.xy.y == 2;
;
