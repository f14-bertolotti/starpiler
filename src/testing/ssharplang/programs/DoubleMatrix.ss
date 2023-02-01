
class DoubleMatrix {

    var double[] data;
    var int64 size;

    fun (DoubleMatrix,int64->DoubleMatrix) __init__(this, size) {
        this.data = new size * size of double;
        this.size = size;
        return this;
    }

    fun (DoubleMatrix,double->DoubleMatrix) fill(this, value) {
        for i from this.size * this.size { this.data[i] = value; }
        return this;
    }

    fun (DoubleMatrix,int64,int64->double) get(this, i, j) {
        return this.data[i * this.size + j];
    }

    fun (->int64) __main__() {
        DoubleMatrix matrix = new DoubleMatrix(10).fill(2.5);
        return matrix.get(2,3) == 2.5;
    }
}
