
struct X with 
    int64 x; 
    int64 y; 
    (X*, int64 -> int64)* increment; 
    (X*, int64, int64 -> X*)* start; 
; 
def int64 incrementX(X* this, int64 x) does 
    return x + this.x + this.y; 
; 
def X* startX(X* this, int64 x, int64 y) does 
    this&.increment = &incrementX; 
    this&.start = &startX; 
    this&.x = x; 
    this&.y = y; 
    return this; 
; 
def int64 start () does 
    X* x = &startX (X{},1 ,2); 
    return x.increment(x, 1); 
;
