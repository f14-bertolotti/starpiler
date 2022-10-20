
tests = {
   "class"         : { "result" : 1, "program" : 
                      """
                      class X with
                          def int64 a;
                          def int64 b;
                          def X* start(X* this, int64 a, int64 b) does
                              this&.a = a;
                              this&.b = b;
                              return this;
                          ;
                          def int64 sum(X* this) does return this.a + this.b;;
                      ;
                      def int64 start() does 
                          X* x = new X(1, 2);
                          return x.sum() == 3;
                      ;
                      """},
   "nested_class1" : { "result" : 3, "program" :
                       """
                       class Y with 
                           def int64 x;
                           def int64 y;
                           def Y* start(Y* this, int64 x, int64 y) does
                               this&.x = x;
                               this&.y = y;
                               return this;
                           ;
                           def int64 get_x(Y* this) does return this.x;;
                           def int64 get_y(Y* this) does return this.y;;
                       ;
                       
                       class X with
                       
                           def Y* y;
                       
                           def X* start(X* this, Y* y) does
                               this&.y = y;
                               return this;
                           ;
                       ;
                       
                       
                       def int64 start() does
                           X* x = new X(new Y(1,2));
                           return x.y.get_x() + x.y.get_y();
                       ;
                       """},

   "nested_class2" : { "result": 1, "program": 
                       """
                       class Z with
                           def int64 a;
                           def int64 b;
                           def Z* start(Z* this, int64 a, int64 b) does
                               this&.a = a;
                               this&.b = b;
                               return this;
                           ;
                       ;

                       class Y with
                           def Z* z;
                           def Y* start(Y* this, Z* z) does
                               this&.z = z;
                               return this;
                           ;
                           def int64 get_a(Y* this) does
                               return this.z.a;
                           ;
                           def int64 get_b(Y* this) does
                               return this.z.b;
                           ;
                           def Z* get_z(Y* this) does
                               return this.z;
                           ;
                       ;
                       class X with
                           def Y* y;
                           def X* start(X* this, Y* y) does
                               this&.y = y;
                               return this;
                           ;
                           def int64 get_a(X* this) does
                               return this.y.z.a;
                           ;
                           def int64 get_b(X* this) does
                               return this.y.z.b;
                           ;
                           def Y* get_y(X* this) does
                               return this.y;
                           ;
                       ;
                       def int64 start() does
                           X* x = new X(new Y(new Z(1,2)));
                            
                           return x.get_a() == 1 * 
                                  x.get_b() == 2 *
                                  x.get_y().z.a == 1 *
                                  x.get_y().z.b == 2 * 
                                  x.get_y().get_a() == 1 * 
                                  x.get_y().get_b() == 2 *
                                  x.get_y().get_z().a == 1 *
                                  x.get_y().get_z().b == 2;
                       ;
                       """},

   "nested_class3" : { "result": 1, "program":  
                       """
                       def int8* malloc(int64);
                       def void  free  (int8*);
                       
                       class X with
                          def int64 n;
                          def int64 i;
                          def int8* s;
                          def X*    start(X* this, int64 n) does this&.i = 0; this&.n = n; this&.s = (&malloc)(n * (size of int8)); return this;;
                          def int64  getn(X* this         ) does return this.n;;
                          def void    end(X* this         ) does &free(this.s); return;;
                       ;
                       
                       class A with
                          def X* x;
                          def A*    start(A* this, X* x) does this&.x = x; return this;;
                          def int64  getn(A* this)       does this.x.s&[this.x.i] = 65 as int8; this.x&.i = this.x.i + 1; return this.x.getn();;
                       ;
                       
                       class B with
                          def X* x;
                          def A* a;
                          def B*    start(B* this, X* x, A* a) does this&.x = x; this&.a = a; return this;;
                          def int64  getn(B* this)             does this.x.s&[this.x.i] = 66 as int8; this.x&.i = this.x.i + 1; return this.a.getn();;
                       ;
                       
                       class C with
                          def X* x;
                          def B* b;
                          def C*    start(C* this, X* x, B* b) does this&.x = x; this&.b = b; return this;;
                          def int64  getn(C* this)             does this.x.s&[this.x.i] = 67 as int8; this.x&.i = this.x.i + 1; return this.b.getn();;
                       ;
                       
                       def int64 start() does
                          X* x = new X(10);
                          C* c = new C(x, B* b = new B(x, A* a = new A(x)));
                          c.getn();
                          auto res = x.s[0] as int64 == 67 *
                                 x.s[1] as int64 == 66 *
                                 x.s[2] as int64 == 65;
                          x.end();
                          return res;
                       ;
                       """},

   "extern"        : { "result" : 1, "program" : 
                       """
                       def int8* malloc(int64);
                       def void  free  (int8*);
                       def int64 start() does
                          int8* x = &malloc(8);
                          &free(x);
                          return 1;
                       ;
                       """},
   "sumop"         : {"result" : 1, "program" : 
                      """
                      class SumOp with
                          def int64 a;
                          def int64 b;
                          def SumOp* start(SumOp* this, int64 a, int64 b) does 
                              this&.a = a;
                              this&.b = b;
                              return this;
                          ;
                          def int64 apply(SumOp* this) does
                              return this.a + this.b;
                          ;
                      ;
                      def int64 start() does
                          SumOp* op = new SumOp(1,2);
                          return op.apply() == 3;
                      ;
                      """},
   "sumop_import"  : {"result" : 1, "program" : 
                      """
                      from "src/programs/spplang/SumOp.spp" import SumOp as Sum;
                      def int64 start() does
                          Sum* sum = new Sum(1,2);
                          return sum.apply() == 3;
                      ;
                      """}

}
