
class SmallIntMatrix {

    var int32[] data;
    var int64 size;

    fun (SmallIntMatrix,int64->SmallIntMatrix) __init__(this, size) {
        this.data = new size * size of int32;
        this.size = size;
        return this;
    }

    fun (SmallIntMatrix,int32->SmallIntMatrix) fill(this, value) {
        for i from this.size * this.size { this.data[i] = value; }
        return this;
    }

    fun (SmallIntMatrix,int64,int64->int32) get(this, i, j) {
        return this.data[i * this.size + j];
    }

    fun (->int64) __main__() {
        SmallIntMatrix matrix = new SmallIntMatrix(10).fill(2 as int32);
        return matrix.get(2,3) as int64 == 2;
    }
}
