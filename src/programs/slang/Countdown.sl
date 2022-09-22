def int64 increment(int64 x) does
    int64 y = x + 1;
   return y;
;


def int64 start() does
    int64 result = increment(10);
    return 0;
;
