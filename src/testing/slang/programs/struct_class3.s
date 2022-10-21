
struct Y with 
        int64 x; 
        (Y*, int64 -> Y*)* start; 
        (Y* -> int64)* get_x; 
        ; 

def Y* startY(Y* this, int64 x) does 
        this&.start = &startY; 
        this&.get_x = &get_xY; 
        this&.x = x; 
        return this; 
        ; 

def int64 get_xY(Y* this) does return this.x;; 

struct X with 
        Y* y; 
        (X*, Y* -> X*)* start; 
        (X* -> Y*)* get_y;
        ; 

def X* startX(X* this, Y* y) does 
        this&.start = &startX; 
        this&.get_y = &get_yX;
        this&.y = y; 
        return this; 
        ; 

def Y* get_yX(X* this) does return this.y;; 

def int64 start() does 
        X* x = &startX(X{}, &startY(Y{}, 3)); 
        return (auto _ = (auto _ = x).get_y(_)).get_x(_);
        ;

