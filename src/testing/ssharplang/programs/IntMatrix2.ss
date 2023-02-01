
class IntMatrix {

    var int64[] data;
    var int64 size;

    fun (IntMatrix,int64->IntMatrix) __init__(this, size) {
        this.data = new size * size of int64;
        this.size = size;
        return this;
    }

    fun (IntMatrix,int64->IntMatrix) fill(this, value) {
        for i from this.size * this.size { this.data[i] = value; }
        return this;
    }

    fun (IntMatrix,int64,int64->int64) get(this, i, j) {
        return this.data[i * this.size + j];
    }

    fun (->int64) __main__() {
        IntMatrix matrix = new IntMatrix(10).fill(1);
        return matrix.get(2,3);
    }
}
