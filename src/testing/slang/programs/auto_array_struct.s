
struct XY with int64 x; int64 y; XY* xy;;
def int64 start() does 
    auto x = [XY{x:1, y:2, xy:XY{x:1, y:2, xy:0 as XY*}},
              XY{x:1,y:1,xy: 0 as XY*}];
    auto y = [1,2,3,4];
    return x[0].xy.x;
;
