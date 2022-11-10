def int8 * memcpy ( int8 * , int8 * , int64 ) ;

def ( int8 * , int8 * , int64 -> int8 * ) * __memcpy = & memcpy ;
def int8 * malloc ( int64 ) ;

def ( int64 -> int8 * ) * __malloc = & malloc ;
def void free ( int8 * ) ;

def ( int8 * -> void ) * __free = & free ;
struct SumOp with 
	int64 a ;
	int64 b ;
	( SumOp * , int64 , int64 -> SumOp * ) * start = & start8671090385531682756 ;
	( SumOp * -> int64 ) * apply = & apply8774268492889600366 ;
	( SumOp * -> void ) * end = & end5817124283691218348 ;;

def SumOp * start8671090385531682756 ( SumOp * this , int64 a , int64 b ) does
	this &. a = a ;
	this &. b = b ;
	return this ;;

def int64 apply8774268492889600366 ( SumOp * this ) does
	return this . a + this . b ;;

def void end5817124283691218348 ( SumOp * this ) does
	__free ( this as int8 * ) ;
	return ;;
