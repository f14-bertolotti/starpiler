from "src/testing/ssharplang/programs/Integer.ss" import Integer as Integer; 

class Test{

    fun (Test -> Test) __init__(this) {
        return this;
    }

    fun (Test->void) f1(this) {
        Integer integer = new Integer(1);
        return;
    }

    fun (-> int64) __main__() {
        Test test = new Test();
        test.f1();
        test.f1();
        test.f1();

        gccollect();


        return 1;
    }
}
