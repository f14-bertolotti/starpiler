def int64 increment(int64 x) does
   return x + 1;
;


def int64 start() does
    int64 result = increment(10);
    return result;
;