def int8 * memcpy ( int8 * , int8 * , int64 ) ;

def ( int8 * , int8 * , int64 -> int8 * ) * __memcpy = & memcpy ;
def int8 * malloc ( int64 ) ;

def ( int64 -> int8 * ) * __malloc = & malloc ;
def void free ( int8 * ) ;

def ( int8 * -> void ) * __free = & free ;
def void free ( int8 * ) ;

def int8 * strdup ( int8 * ) ;

def int64 printf ( int8 * , ... ) ;

def int64 sprintf ( int8 * , int8 * , ... ) ;

def int64 strlen ( int8 * ) ;

def int8 * malloc ( int64 ) ;

def int8 * strcpy ( int8 * , int8 * ) ;

def int8 * strncpy ( int8 * , int8 * , int64 ) ;

def int64 strcmp ( int8 * , int8 * ) ;

def int64 abs ( int64 ) ;

def double log10 ( double ) ;

def double ceil ( double ) ;

struct String with 
	int8 * mem ;
	int64 length ;
	( String * , int8 * -> String * ) * start = & start3608241247340427601 ;
	( String * -> String * ) * print = & print327085397788944921 ;
	( String * , int64 -> String * ) * repeat = & repeat4376566696847837673 ;
	( String * , String * -> int64 ) * equals = & equals5500345735686460839 ;
	( String * , int64 , int64 -> String * ) * substring = & substring4328121212589501564 ;
	( String * , String * -> String * ) * catFromString = & catFromString7712737417195542972 ;
	( String * , int8 * -> String * ) * catFromInt8ptr = & catFromInt8ptr2732254027814851598 ;
	( String * , int64 -> String * ) * catFromInt64 = & catFromInt644032785904053193867 ;
	( String * , int64 -> String * ) * fromInt64 = & fromInt645438506568561954931 ;
	( String * -> void ) * end = & end952120263426887198 ;;

def String * start3608241247340427601 ( String * this , int8 * value ) does
	this &. mem = & strdup ( value ) ;
	this &. length = & strlen ( value ) ;
	return this ;;

def String * print327085397788944921 ( String * this ) does
	& printf ( this . mem ) ;
	return this ;;

def String * repeat4376566696847837673 ( String * this , int64 times ) does
	int8 * ptr = & malloc ( this . length * times + 1 ) ;
	int64 rep = 0 ;
	while rep < times do 	int8 * cur = ptr &[ this . length * rep ] ;
	& strncpy ( cur , this . mem , this . length ) ;
	& rep = rep + 1 ; ;
	& free ( this . mem ) ;
	this &. mem = ptr ;
	this &. length = this . length * times ;
	return this ;;

def int64 equals5500345735686460839 ( String * this , String * other ) does
	if & strcmp ( this . mem , other . mem ) == 0 do 	return 1 ; ;
	return 0 ;;

def String * substring4328121212589501564 ( String * this , int64 a , int64 b ) does
	if a > b do 	return 0 as String * ; ;
	if a > this . length do 	return 0 as String * ; ;
	int8 * ptr = & malloc ( ( b - a ) + 1 ) ;
	& strncpy ( ptr , this . mem &[ a ] , b - a ) ;
	ptr &[ b - a ] = 0 as int8 ;
	& free ( this . mem ) ;
	this &. mem = ptr ;
	this &. length = ( b - a ) ;
	return this ;;

def String * catFromString7712737417195542972 ( String * this , String * other ) does
	int8 * ptr = & malloc ( this . length + other . length + 1 ) ;
	& strncpy ( ptr , this . mem , this . length ) ;
	& strcpy ( ptr &[ this . length ] , other . mem ) ;
	& free ( this . mem ) ;
	this &. mem = ptr ;
	this &. length = this . length + other . length ;
	return this ;;

def String * catFromInt8ptr2732254027814851598 ( String * this , int8 * other ) does
	int64 otherlen = & strlen ( other ) ;
	int8 * ptr = & malloc ( this . length + otherlen + 1 ) ;
	& strncpy ( ptr , this . mem , this . length ) ;
	& strcpy ( ptr &[ this . length ] , other ) ;
	& free ( this . mem ) ;
	this &. mem = ptr ;
	this &. length = this . length + otherlen ;
	return this ;;

def String * catFromInt644032785904053193867 ( String * this , int64 other ) does
	int64 digits = & ceil ( & log10 ( ( & abs ( other ) + 1 ) as double ) ) as int64 ;
	int8 * buffer = & malloc ( digits + 1 ) ;
	& sprintf ( buffer , "%d\0" , other ) ;
	( auto __ = this ) . catFromInt8ptr ( __ , buffer ) ;
	& free ( buffer ) ;
	return this ;;

def String * fromInt645438506568561954931 ( String * this , int64 value ) does
	int64 digits = & ceil ( & log10 ( ( & abs ( value ) + 1 ) as double ) ) as int64 ;
	int8 * buffer = & malloc ( digits + 1 ) ;
	& sprintf ( buffer , "%d\0" , value ) ;
	& free ( this . mem ) ;
	this &. mem = buffer ;
	this &. length = digits ;
	return this ;;

def void end952120263426887198 ( String * this ) does
	& free ( this . mem ) ;
	return ;;
