from "src/testing/ssharplang/programs/Integer.ss" import Integer as Integer; 
from "src/testing/ssharplang/programs/IntArray.ss" import IntArray as IntArray;

class IntMatrix {

    var IntArray[] rows;
    var int64 size;

    fun (IntMatrix, int64 -> IntMatrix) __init__(this, size) {
        this.rows = new size of IntArray(size);
        this.size = size;
        return this;
    }

    fun (IntMatrix, int64 -> IntMatrix) fill(this, value) {
        for i from this.size { this.rows[i].fill(value); }
        return this;
    }

    fun (IntMatrix, int64, int64 -> int64) get(this, i, j) {
        return this.rows[i].get(j);
    }

    fun (-> int64) __main__() {
        IntMatrix matrix = new IntMatrix(3).fill(1);
        return matrix.get(0,0) == 1 * matrix.get(2,2) == 1;
    }
}
