from "src/testing/slang/programs/Increment.s" import increment as increment;

def int64 doubleIncrement(int64 x) does
   return &increment(&increment(x));
;
