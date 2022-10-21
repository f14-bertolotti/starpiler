
struct Y with 
        int64 x; 
        int64 y; 
        (Y*, int64, int64 -> Y*)* start; 
        (Y* -> int64)* get_x; 
        (Y* -> int64)* get_y; 
        ; 

def Y* startY(Y* this, int64 x, int64 y) does 
        this&.start = &startY; 
        this&.get_x = &get_xY; 
        this&.get_y = &get_yY; 
        this&.x = x; 
        this&.y = y; 
        return this; 
        ; 

def int64 get_xY(Y* this) does return this.x;; 
def int64 get_yY(Y* this) does return this.y;; 

struct X with 
        Y* y; 
        (X*, Y* -> X*)* start; 
        ; 

def X* startX(X* this, Y* y) does 
        this&.start = &startX; 
        this&.y = y; 
        return this; 
        ; 

def int64 start() does 
        X* x = &startX(X{}, &startY(Y{}, 1, 2)); 
        auto _1 = x.y; 
        auto _2 = x.y; 
        return _1.get_x(_1) + _2.get_y(_2) ; 
        ;

