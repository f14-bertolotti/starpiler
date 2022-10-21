
struct XY with int8* string;;

def int32 printf(int8*, ...);

def int64 start() does 
    XY** xys = [XY{string:"aaa"}, XY{string:"aaa"}];
    return (xys[0].string[0] as int64 == xys[1].string[0] as int64) * 
           (xys[0].string[1] as int64 == xys[1].string[1] as int64) *
           (xys[0].string[2] as int64 == xys[1].string[2] as int64);
;
