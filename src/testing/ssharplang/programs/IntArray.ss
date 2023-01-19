
class IntArray {

    var int64[] data;
    var int64   size;

    fun (IntArray, int64 -> IntArray) __init__(this, size) {
        this.size = size;
        this.data = new size of int64();
        return this;
    } 

    fun (-> int64) __main__() {
        IntArray array = new IntArray(100); 
        return 0;
    }
}


