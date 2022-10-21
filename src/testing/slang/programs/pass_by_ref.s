
def int64 f(int64* x) does x = x[0] + 1; return 0;;
def int64 start() does int64 x = 0; &f(&x); return x;;
