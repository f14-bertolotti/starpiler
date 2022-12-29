class Simple {

    var int64 x;

    fun (int64->void) init() {
        x = 0;
    }

    fun (->int64) increment() {
        x = x + 1;
    }

}
