
def void f(int64* x) does x = x[0]+1; return;;
def int64 start() does int64 x = 0; &f(&x); return x;;
