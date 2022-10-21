from "src/testing/slang/programs/Increment.s" import increment as inc;

def int64 doubleIncrement(int64 x) does
   return &inc(&inc(x));
;
