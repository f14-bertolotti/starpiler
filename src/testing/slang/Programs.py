pointer1 = """
def int8* malloc(int64);
def void free(int8*);

def int64 start() does
    int64* x = &malloc(8 * 3) as int64*;
    x&[0] = 0;
    x&[1] = 0;
    x&[2] = 0;
    int64 a = x[0];
    int64 b = x[1];
    int64 c = x[2];
    &free(x as int8*);
    return a == b * b == c * c == 0;
;
"""

pointer2 = """
def int8* malloc(int64);
def void free(int8*);

def int64 start() does
    int64** x = &malloc(8 * 3) as int64**;
    x&[0] = &malloc(8 * 3) as int64*;
    x&[1] = &malloc(8 * 3) as int64*;
    x&[2] = &malloc(8 * 3) as int64*;
    x[0]&[0] = 0;
    x[0]&[1] = 1;
    x[0]&[2] = 2;
    x[1]&[0] = 3;
    x[1]&[1] = 4;
    x[1]&[2] = 5;
    x[2]&[0] = 6;
    x[2]&[1] = 7;
    x[2]&[2] = 8;
    int64 result = x[0][0] == 0 * 
                   x[0][1] == 1 * 
                   x[0][2] == 2 *
                   x[1][0] == 3 *
                   x[1][1] == 4 *
                   x[1][2] == 5 *
                   x[2][0] == 6 *
                   x[2][1] == 7 *
                   x[2][2] == 8;

    &free(x[0] as int8*);
    &free(x[1] as int8*);
    &free(x[2] as int8*);
    &free(x as int8*);

    return result;
;
"""

while3 = """
def int64 start() does
    int64 x = 10;
    while x != 0 do
        &x = x - 1;
    ;
    return x;
;
"""

printf1 = """
def int32 printf(int8*, ...);
def int8* malloc(int64);
def void free(int8*);

def int64 start() does
    int8* f = &malloc(3) as int8*;
    int8* s = &malloc(1) as int8*;
    s&[0] = 65 as int8;
    s&[1] = 65 as int8;
    s&[2] = 0 as int8;
    f&[0] = 0 as int8;
    &printf(f,s);
    &free(f);
    &free(s);
    return 0;
;            
"""          
             
printf2 = """
def int32 printf(int8*, ...);
def int64 start() does
    &printf(\"%s\",\"\");
    return 0;
;
"""


array1 = """
def int64 start() does
    int64* x = [1,2,3,4];
    int64** y = [[1,2,3],[1,2]];
    return x[0] == 1 * 
           x[1] == 2 *
           x[2] == 3 *
           x[3] == 4 *
           y[0][0] == 1 *
           y[0][1] == 2 *
           y[0][2] == 3 *
           y[1][0] == 1 *
           y[1][1] == 2;
;
"""

array2 = """
def int64 start() does
    int64* x = [1,2];
    int64** y = [x,x];
    return x[0] == 1 * 
           x[1] == 2 *
           y[0][0] == 1 *
           y[0][1] == 2 *
           y[1][0] == 1 *
           y[1][1] == 2;
;
"""

array3 = """
def int8* malloc(int64);
def void free(int8*);
def int8* memcpy(int8*,int8*,int32); 

def int64 start() does
    int64* x = [1,2,3,4,5];
    int64* y = &malloc(8 * 5) as int64*;
    &memcpy(y as int8*, x as int8*, (8 * 5) as int32);
    int64 result = y[0] == 1 * 
                   y[1] == 2 *
                   y[2] == 3 *
                   y[3] == 4 *
                   y[4] == 5;
    &free(y as int8*);
    return result;
;
"""

globalValue = """
def int64 x = 0;
def int64 y = 1;
def int64* z = [x + y,2,3,4];
def int64 start() does
    int64 result = x == 0 * y == 1 * 
             z[0] == 1 *
             z[1] == 2 *
             z[2] == 3 *
             z[3] == 4;
    return result;
;
"""

import1 = """
from "src/programs/slang/Increment.sl" import increment as inc;
from "src/programs/slang/Increment.sl" import x as y;

def int64 start() does
    return &inc(y);
;
"""

import2 = """
from "src/programs/slang/DoubleDoubleIncrement.sl" import doubleDoubleIncrement as inc;

def int64 start() does
    return &inc(0);
;
"""

import3 = """
from "src/programs/slang/DoubleDoubleIncrement.sl" import doubleDoubleIncrement as inc;
from "src/programs/slang/Shape2Sides.sl" import triangle as triangle;
from "src/programs/slang/Shape2Sides.sl" import square as square;

def int64 start() does
    return &inc(triangle + square);
;
"""

ftype1 = """
def int64 increment(int64 x) does
    return x + 1;
;

def int64 start() does
    int8* f = &increment as int8*;
    return (f as (int64 -> int64)*)(0);
;
"""

extern1 = """
def int32 printf(int8*, ...);

def int64 start() does
    &printf("%s","");
    return 0;
;
"""
comment = """
def int64 start() does
    # A COMMENT
    return 0;
;
"""

variable_declaration2 = """
def int64 x;
def int64 start() does
    &x = 1;
    return x;
;
"""

recursive = """
def int64 fib(int64 n) does
    if n == 0 do return 0;;
    if n == 1 do return 1;;
    return (&fib(n - 1)) + (&fib(n - 2));
;
def int64 start() does
    return &fib(12);
;
"""

pass_by_value = """
def int64 f(int64 x) does &x = x + 1; return 0;;
def int64 start() does int64 x = 0; &f(x); return x;;
"""

pass_by_ref = """
def int64 f(int64* x) does x = x[0] + 1; return 0;;
def int64 start() does int64 x = 0; &f(&x); return x;;
"""

voidfunc = """
def void f(int64* x) does x = x[0]+1; return;;
def int64 start() does int64 x = 0; &f(&x); return x;;
"""

struct = """
struct XY with
    int64 x;
    int8* y;
;

def int64 start() does
    XY* xy = XY{x:1, y:0 as int8*};
    return xy.x;
;
"""

nested_struct = """
struct XY with
    int64 x;
    int64 y;
    XY*  xy;
;

def int64 start() does
    XY* xy = XY{x:1, y:1, xy:XY{x:2, y:2, xy:0 as XY*}};
    return xy.x == 1 *
           xy.y == 1 *
           xy.xy.x == 2 *
           xy.xy.y == 2;
;
"""

array_struct = """
struct XY with int8* string;;

def int32 printf(int8*, ...);

def int64 start() does 
    XY** xys = [XY{string:"aaa"}, XY{string:"aaa"}];
    return (xys[0].string[0] as int64 == xys[1].string[0] as int64) * 
           (xys[0].string[1] as int64 == xys[1].string[1] as int64) *
           (xys[0].string[2] as int64 == xys[1].string[2] as int64);
;
"""

import_struct1 = """
from "src/programs/slang/XYStruct.sl" import XY as ZZ;

def int64 start() does
    ZZ* zz = ZZ{x:0,y:0,xy:0 as ZZ*};
    return zz.x;
;
"""

import_struct2 = """
from "src/programs/slang/XYZStruct.sl" import XYZ as Two;
from "src/programs/slang/XYStruct.sl" import XY as One;

def int64 start() does 
    One* one = One{x:0,y:1,xy:0 as One*};
    Two* two = Two{x:3, xy:one};
    return two.xy.y;
;
"""

double_import_function = """
from "src/programs/slang/Increment.sl" import increment as incr;
from "src/programs/slang/DoubleIncrement3.sl" import doubleIncrement as dincr;

def int64 start() does
    return &dincr(&incr(0));
;
"""

auto = """
def int64 start() does 
    auto x = 10;
    return x;
;
"""

auto_struct = """
struct XY with int64 x; int64 y; XY* xy;;

def int64 start() does 
    auto x = XY{x:0, y:1, xy:0 as XY*};
    return x.y;
;
"""

auto_nested_struct = """
struct XY with int64 x; int64 y; XY* xy;;

def int64 start() does
    auto y = XY{x:1, y:2, xy:XY{x:1, y:2, xy:0 as XY*}};
    return y.xy.y;
;
"""

auto_array = """
struct XY with int64 x; int64 y; XY* xy;;
def int64 start() does
    auto y = [1,2,3,4];
    return y[2];
;
"""

auto_array_struct = """
struct XY with int64 x; int64 y; XY* xy;;
def int64 start() does 
    auto x = [XY{x:1, y:2, xy:XY{x:1, y:2, xy:0 as XY*}},
              XY{x:1,y:1,xy: 0 as XY*}];
    auto y = [1,2,3,4];
    return x[0].xy.x;
;
"""

auto_func = """
def int64 increment(int64 x) does return x + 1;;
def int64 apply(int8* f, int64 value) does return (f as (int64 -> int64)*)(value);;
def int64 start() does 
    auto f = &increment;
    return &apply(f as int8*, 10);
;
"""

tests = {
            "increment"              : {"program" : "def int64 increment(int64 x) does return x + 1;; def int64 start() does int64 result = &increment(10); return result;;", "result"  : 11},
            "mutableVars"            : {"program" : " def int64 start() does int64 x = 10; &x = 11; return x;; ", "result" : 11},
            "multiplication"         : {"program" : " def int64 start() does return 10 * 10;;", "result" : 100},
            "division"               : {"program" : " def int64 start() does return 100 / 10;;", "result" : 10},
            "floatDivision"          : {"program" : "def double start() does return 100.0 / 10.0;;", "result":10.0},
            "floatMultiplication"    : {"program" : "def double start() does return 10.0 * 10.0;;", "result":100.0},
            "subfloat"               : {"program" : "def double start() does return (1.0 - 1.5);;", "result":-0.5},
            "cast1"                  : {"program" : "def double start() does return 1 as double;;", "result":1.0},
            "negation"               : {"program" : "def int64 start() does return -10;;", "result":-10},
            "floatNegation"          : {"program" : "def double start() does return -10.0;;", "result":-10.0},
            "modulo"                 : {"program" : "def int64 start() does return 10 % 4;;", "result":2},
            "floatModulo"            : {"program" : "def double start() does return 10.0 % 4.0;;", "result":2.0},
            "equality1"              : {"program" : "def int64 start() does return 10 == 10;;", "result":1},
            "equality2"              : {"program" : "def int64 start() does return 10 == 0;;", "result":0},
            "floatEquality1"         : {"program" : "def int64 start() does return 10.0 == 10.0;;", "result":1},
            "floatEquality2"         : {"program" : "def int64 start() does return 10.0 == 0.0;;", "result":0},
            "nequality1"             : {"program" : "def int64 start() does return 10 != 10;;", "result":0},
            "nequality2"             : {"program" : "def int64 start() does return 10 != 0;;", "result":1},
            "floatNequality1"        : {"program" : "def int64 start() does return 10.0 != 10.0;;", "result":0},
            "floatNequality2"        : {"program" : "def int64 start() does return 10.0 != 0.0;;", "result":1},
            "expression1"            : {"program" : "def int64 start() does return -10 * 10 + 10;;", "result":-90},
            "expression1F"           : {"program" : "def double start() does return -10.0 * 10.0 + 10.0;;", "result":-90.0},
            "expression2"            : {"program" : "def int64 start() does return -10 * 10 + 10 * 10;;", "result":0},
            "expression2F"           : {"program" : "def double start() does return -10.0 * 10.0 + 10.0 * 10.0;;", "result":0},
            "expression3"            : {"program" : "def int64 start() does return -10 * 10 / 2 + 10 * 10;;", "result":50},
            "expression3F"           : {"program" : "def double start() does return -10.0 * 10.0 / 2.0 + 10.0 * 10.0;;", "result":50.0},
            "expression4"            : {"program" : "def int64 start() does return 4.0 > (2 as double);;", "result":1},
            "expression_gte1"        : {"program" : "def int64 start() does return 4.0 >= (4 as double);;", "result":1},
            "expression_gte2"        : {"program" : "def int64 start() does return 4 >= 2;;", "result":1},
            "expression_lss1"        : {"program" : "def int64 start() does return 4.0 < (4 as double);;", "result":0},
            "expression_lss2"        : {"program" : "def int64 start() does return 4 < 2;;", "result":0},
            "expression_leq1"        : {"program" : "def int64 start() does return 4.0 <= (4 as double);;", "result":1},
            "expression_leq2"        : {"program" : "def int64 start() does return 4 <= 2;;", "result":0},
            "ifthen1"                : {"program" : "def int64 start() does if 1 == 1 do return 1;; return 0;;", "result":1},
            "ifthen2"                : {"program" : "def int64 start() does if 0 == 1 do return 1;;return 0;;", "result":0},
            "ifthen3"                : {"program" : "def int64 start() does if 1 == 1 do if 2 == 2 do return 2;; return 1;; return 0;;", "result":2},
            "ifthen4"                : {"program" : "def int64 start() does if 1 == 1 do if 2 == 1 do return 2;;return 1;;return 0;;", "result":1},
            "ifthen5"                : {"program" : "def int64 start() does if 1 == 0 do return 1;; if 2 == 0 do return 2;; if 3 == 0 do return 3;; return 0; ;", "result":0},
            "ifthen6"                : {"program" : "def int64 start() does if 1 == 0 do return 1;; if 2 == 2 do return 2;; if 3 == 0 do return 3;; return 0; ;", "result":2},
            "ifthen62"               : {"program" : "def int64 start() does int64 x = 10; int64 y = 9; if x != y do &y = x;; return y; ;", "result":10},
            "ifthen7"                : {"program" : "def int64 start() does int64 x = 5+5; int64 y = 4+5; if x != y do &y = y + 1;; return y; ;", "result":10},
            "ifthen8"                : {"program" : "def int64 start() doesint64 x = 10; int64 y = 5; if x != y do int64 y = y + 1;; return y; ;", "result":5},
            "while1"                 : {"program" : "def int64 start() does int64 x = 10; int64 y = 9; while x != y do &y = x;; return y; ;", "result":10},
            "while2"                 : {"program" : "def int64 start() does int64 x = 10; int64 y = 5; while x != y do &y = y + 1;; return y;;", "result":10},
            "while3"                 : {"program" : while3,"result":0},
            "pointer1"               : {"program" : pointer1,"result":1},
            "pointer2"               : {"program" : pointer2,"result":1},
            "printf1"                : {"program" : printf1,"result":0},
            "printf2"                : {"program" : printf2,"result":0},
            "array1"                 : {"program" : array1,"result":1},
            "array2"                 : {"program" : array2,"result":1},
            "array3"                 : {"program" : array3,"result":1},
            "globalValue"            : {"program" : globalValue,"result":1},
            "import1"                : {"program" : import1,"result":1},
            "import2"                : {"program" : import2,"result":4},
            "import3"                : {"program" : import3,"result":11},
            "ftype1"                 : {"program" : ftype1,"result":1},
            "extern1"                : {"program" : extern1,"result":1},
            "comment"                : {"program" : comment,"result":11},
            "variable_declaration2"  : {"program":variable_declaration2,"result":1},
            "recursive"              : {"program":recursive,"result":144},
            "pass_by_value"          : {"program":pass_by_value,"result":0},
            "pass_by_ref"            : {"program":pass_by_ref,"result":1},
            "voidfunc"               : {"program":voidfunc,"result":1},
            "struct"                 : {"program":struct,"result":1},
            "nested_struct"          : {"program":nested_struct,"result":1},
            "array_struct"           : {"program":array_struct,"result":1},
            "import_struct1"         : {"program":import_struct1,"result":0},
            "import_struct2"         : {"program":import_struct2,"result":1},
            "double_import_function" : {"program":double_import_function,"result":3},
            "auto"                   : {"program":auto,"result":10},
            "auto_struct"            : {"program":auto_struct,"result":1},
            "auto_nested_struct"     : {"program":auto_nested_struct,"result":2},
            "auto_func"              : {"program":auto_func,"result":3},
            "auto_array_struct"      : {"program":auto_array_struct,"result":0},
            "auto_array"             : {"program":auto_array,"result":0},

        }


