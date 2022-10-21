
from "src/testing/slang/programs/XYZStruct.s" import XYZ as Two;
from "src/testing/slang/programs/XYStruct.s" import XY as One;

def int64 start() does 
    One* one = One{x:0,y:1,xy:0 as One*};
    Two* two = Two{x:3, xy:one};
    return two.xy.y;
;
