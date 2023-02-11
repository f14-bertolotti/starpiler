from "src/testing/ssharplang/programs/FFI.ss" import FFI as FFI; 

class Stack {
 
    fun (Stack->Stack) __init__(this) {
        return this;
    }

    fun (->void) f() {
        print("Hello");
        return;
    }

    fun (->int64) __main__() {
        FFI ffi = new FFI();
        int8[] buffer = ffi.malloc(size of Stack);
        ffi.free(buffer);
        return 1;
    }    
}
