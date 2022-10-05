from "src/programs/slang/DoubleIncrement2.sl" import doubleIncrement as doubleIncrement;

def int64 doubleDoubleIncrement(int64 x) does
   return doubleIncrement(doubleIncrement(x));
;
