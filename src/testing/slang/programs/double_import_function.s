
from "src/testing/slang/programs/Increment.s" import increment as incr;
from "src/testing/slang/programs/DoubleIncrement3.s" import doubleIncrement as dincr;

def int64 start() does
    return &dincr(&incr(0));
;
