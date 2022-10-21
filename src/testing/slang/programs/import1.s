
from "src/testing/slang/programs/Increment.s" import increment as inc;
from "src/testing/slang/programs/Increment.s" import x as y;

def int64 start() does
    return &inc(y);
;
