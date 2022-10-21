from "src/testing/slang/programs/DoubleIncrement2.s" import doubleIncrement as doubleIncrement;

def int64 doubleDoubleIncrement(int64 x) does
   return &doubleIncrement(&doubleIncrement(x));
;
