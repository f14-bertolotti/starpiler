
struct Y with
        int64 x;
        int64 y;
;

struct X with
        int64 x;
        int64 y;
        Y* y;
;

def int64 start() does return size of X;;
