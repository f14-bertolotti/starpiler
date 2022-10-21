from "src/testing/slang/programs/Increment.s" import increment;

def int64 start() does
    int64 result = &increment(10);
    return result;
;
