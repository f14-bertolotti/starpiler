from "src/testing/ssharplang/programs/Integer.ss" import Integer as Integer; 

class IntArray {

    var Integer[] data;
    var int64     size;

    fun (IntArray, int64 -> IntArray) __init__(this, size) {
        this.size = size;
        this.data = new size of Integer(0);
        return this;
    } 

    fun (IntArray, int64 -> IntArray) fill(this, value) {
        for i from this.size {
            this.data[i].value = value;
        }
        return this;
    }

    fun (IntArray, int64 -> int64) get(this, i) {
        return this.data[i].value;
    }

    fun (-> int64) __main__() {
        IntArray array = new IntArray(100).fill(10); 
        int64 i = 0;
        int64 result = 1;
        while (i < array.size) {
            result = result * (array.get(i) == 10); 
            i = i + 1;
        }

        return result;
    }
}


