from "src/programs/slang/Increment.sl" import increment as increment;

def int64 doubleIncrement(int64 x) does
   return increment(increment(x));
;
