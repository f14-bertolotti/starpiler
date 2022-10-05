def int64 increment(int64 x) does
   return x + 1;
;

def int64 doubleIncrement(int64 x) does
   return increment(increment(x));
;
