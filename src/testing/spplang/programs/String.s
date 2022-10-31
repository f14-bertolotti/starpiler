def void free ( int8 * ) ; def int8 * strdup ( int8 * ) ; def int64 printf ( int8 * , ... ) ; def int64 sprintf ( int8 * , int8 * , ... ) ; def int64 strlen ( int8 * ) ; def int8 * malloc ( int64 ) ; def int8 * strcpy ( int8 * , int8 * ) ; def int8 * strncpy ( int8 * , int8 * , int64 ) ; def int64 strcmp ( int8 * , int8 * ) ; def int64 abs ( int64 ) ; def double log10 ( double ) ; def double ceil ( double ) ; struct String with int8 * mem ; int64 length ; ( String * , int8 * -> String * ) * start = & _1_start ; ( String * -> String * ) * print = & _2_print ; ( String * , int64 -> String * ) * repeat = & _3_repeat ; ( String * , String * -> int64 ) * equals = & _4_equals ; ( String * , int64 , int64 -> String * ) * substring = & _5_substring ; ( String * , String * -> String * ) * catFromString = & _6_catFromString ; ( String * , int8 * -> String * ) * catFromInt8ptr = & _7_catFromInt8ptr ; ( String * , int64 -> String * ) * fromInt64 = & _8_fromInt64 ; ( String * -> void ) * end = & _9_end ; ; def String * _1_start ( String * this , int8 * value ) does this &. mem = & strdup ( value ) ; this &. length = & strlen ( value ) ; return this ; ; def String * _2_print ( String * this ) does & printf ( this . mem ) ; return this ; ; def String * _3_repeat ( String * this , int64 times ) does int8 * ptr = & malloc ( ( this . length - 1 ) * times + 1 ) ; int64 rep = 0 ; while rep < times do int8 * cur = ptr &[ this . length * rep ] ; & strcpy ( cur , this . mem ) ; & rep = rep + 1 ; ; & free ( this . mem ) ; this &. mem = ptr ; this &. length = this . length * times ; return this ; ; def int64 _4_equals ( String * this , String * other ) does if & strcmp ( this . mem , other . mem ) == 0 do return 1 ; ; return 0 ; ; def String * _5_substring ( String * this , int64 a , int64 b ) does if a > b do return 0 as String * ; ; if a > this . length do return 0 as String * ; ; int8 * ptr = & malloc ( ( b - a ) + 1 ) ; & strncpy ( ptr , this . mem &[ a ] , b - a ) ; ptr &[ b - a ] = 0 as int8 ; & free ( this . mem ) ; this &. mem = ptr ; this &. length = ( b - a ) ; return this ; ; def String * _6_catFromString ( String * this , String * other ) does int8 * ptr = & malloc ( this . length + other . length + 1 ) ; & strncpy ( ptr , this . mem , this . length ) ; & strcpy ( ptr &[ this . length ] , other . mem ) ; & free ( this . mem ) ; this &. mem = ptr ; this &. length = this . length + other . length ; return this ; ; def String * _7_catFromInt8ptr ( String * this , int8 * other ) does int64 otherlen = & strlen ( other ) ; int8 * ptr = & malloc ( this . length + otherlen + 1 ) ; & strncpy ( ptr , this . mem , this . length ) ; & strcpy ( ptr &[ this . length ] , other ) ; & free ( this . mem ) ; this &. mem = ptr ; this &. length = this . length + otherlen ; return this ; ; def String * _8_fromInt64 ( String * this , int64 value ) does int64 digits = & ceil ( & log10 ( ( & abs ( value ) + 1 ) as double ) ) as int64 ; int8 * buffer = & malloc ( digits + 1 ) ; & sprintf ( buffer , "%d\0" , value ) ; & free ( this . mem ) ; this &. mem = buffer ; this &. length = digits ; return this ; ; def void _9_end ( String * this ) does & free ( this . mem ) ; return ; ;