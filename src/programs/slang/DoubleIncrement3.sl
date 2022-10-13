from "src/programs/slang/Increment.sl" import increment as inc;

def int64 doubleIncrement(int64 x) does
   return &inc(&inc(x));
;
