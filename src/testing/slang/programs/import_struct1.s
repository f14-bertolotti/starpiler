
from "src/testing/slang/programs/XYStruct.s" import XY as ZZ;

def int64 start() does
    ZZ* zz = ZZ{x:0,y:0,xy:0 as ZZ*};
    return zz.x;
;
