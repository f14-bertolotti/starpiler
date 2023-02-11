
class FFI {

    fun (FFI -> FFI) __init__(this){
        return this;
    }

    fun (FFI, int64 -> int8[]) malloc(this, size) {
        return __malloc__(size);
    }

    fun (FFI, int8[]->void) free(this, ptr) {
        __free__(ptr);
        return;
    }

}

