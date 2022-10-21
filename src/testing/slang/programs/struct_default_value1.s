
struct X with 
        int64 x = 12;
;

def int64 start() does
        return X{}.x == 12;
;
