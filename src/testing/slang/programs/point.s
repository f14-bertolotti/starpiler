def void free ( int8 * ) ;
def int8 * memcpy ( int8 * , int8 * , int64 ) ;
def int8 * malloc ( int64 ) ;

struct Point with 
     double x ;
	 double y ;
	 ( Point * , double , double -> Point * ) * start = & _1_start ;
	 ( Point * , double , double -> Point * ) * set = & _2_set ;
	 ( Point * -> void ) * end = & _3_end ;
;

def Point * _1_start ( Point * this , double x , double y ) does 
   this &. x = x ;
   this &. y = y ;
   return this ;
;

def Point * _2_set ( Point * this , double x , double y ) does 
   this &. x = x ;
   this &. y = y ;
   return this ;
;

def void _3_end ( Point * this ) does 
    &free(this as int8*);
    return ;
;

def int64 start ( ) does 
     Point* point_heap = (auto _0_ = &memcpy(&malloc(size of Point), 
                                             Point{} as int8*, 
                                             size of Point) as Point*).start(_0_, 0.0 ,0.0);
	 Point* point_stack = Point{x: 1.0, y: 1.0};
	 (auto _0_ = point_stack).set(_0_, 0.0, 0.0);
	 int64 result = ((point_stack.x == point_heap.x) as int64) * 
                    ((point_stack.y == point_heap.y) as int64) ;
	 (auto _0_ = point_heap).end(_0_);
	 return result ;
;
	

