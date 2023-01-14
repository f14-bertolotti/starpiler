class Simple {

    var int64 x;

    fun (Simple, int64->Simple) __init__(this,x) {
        this.x = 0;
        return;
    }

    fun (->int64) increment() {
        x = x + 1;
        return x;
    }

}
