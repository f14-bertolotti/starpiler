
class CharMatrix {

    var int8[] data;
    var int64 size;

    fun (CharMatrix,int64->CharMatrix) __init__(this, size) {
        this.data = new size * size of int8;
        this.size = size;
        return this;
    }

    fun (CharMatrix,int8->CharMatrix) fill(this, value) {
        for i from this.size * this.size { this.data[i] = value; }
        return this;
    }

    fun (CharMatrix,int64,int64->int8) get(this, i, j) {
        return this.data[i * this.size + j];
    }

    fun (->int64) __main__() {
        CharMatrix matrix = new CharMatrix(10).fill(2 as int8);
        return matrix.get(2,3) as int64 == 2;
    }
}
