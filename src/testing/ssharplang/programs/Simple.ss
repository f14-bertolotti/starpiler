from "src/testing/ssharplang/programs/simple_class.ss" import Simple as S ;
class A {
    var int64 x;
    fun (A, int64 -> A) __init__(this, x) {
        this.x = x;
        return this;
    }
    fun ( -> int64) __main__ () {
        S s = new S(1);
        return s.x;
    }
}

