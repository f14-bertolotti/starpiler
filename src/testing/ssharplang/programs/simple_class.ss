class Simple {

    var int64 x;

    fun (Simple, int64->Simple) __init__(this,x) {
        this.x = x;
        return this;
    }

    fun (Simple->int64) increment(this) {
        this.x = this.x + 1;
        return this.x;
    }

}
