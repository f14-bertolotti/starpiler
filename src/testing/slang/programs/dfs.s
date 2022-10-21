def int8* malloc(int64);
def void free(int8*);

def int8** n0 = [[10] as int8*, 0  as int8*, 0  as int8*];
def int8** n1 = [[9 ] as int8*, 0  as int8*, 0  as int8*];
def int8** n2 = [[8 ] as int8*, n0 as int8*, n1 as int8*];

def int8** n3 = [[7 ] as int8*, 0  as int8*, 0  as int8*];
def int8** n4 = [[6 ] as int8*, 0  as int8*, 0  as int8*];
def int8** n5 = [[5 ] as int8*, n3 as int8*, n4 as int8*];

def int8** n6 = [[4 ] as int8*, n2 as int8*, n5 as int8*];

def int64* res = [0,0,0,0,0,0,0];

def int64 visit(int8** node, int64 i) does
    if (node as int64) == 0 do return i-1;;

    res&[i] = (node[0] as int64*)[0];

    &i = &visit(node[1] as int8**, i + 1);
    &i = &visit(node[2] as int8**, i + 1);

    return i;
;

def int64 start() does
    &visit(n6,0); 
    return res[0] == 4  *
           res[1] == 8  *
           res[2] == 10 *
           res[3] == 9  *
           res[4] == 5  *
           res[5] == 7  *
           res[6] == 6;
;

