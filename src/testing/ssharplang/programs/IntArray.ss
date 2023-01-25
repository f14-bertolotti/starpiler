from "src/testing/ssharplang/programs/Integer.ss" import Integer as Integer; 

class IntArray {

    var Integer[] data;
    var int64     size;

    fun (IntArray, int64 -> IntArray) __init__(this, size) {
        this.size = size;
        this.data = new size of Integer(10);
        return this;
    } 

    fun (-> int64) __main__() {
        IntArray array = new IntArray(100); 
        return 0;
    }
}


