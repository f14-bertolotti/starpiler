
def int64 fib(int64 n) does
    if n == 0 do return 0;;
    if n == 1 do return 1;;
    return (&fib(n - 1)) + (&fib(n - 2));
;
def int64 start() does
    return &fib(12);
;
