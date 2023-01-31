class Integer {
    
    var int64 value;

    fun (Integer, int64 -> Integer) __init__ (this, value) {
        this.value = value;
        return this;
    }

    fun (Integer, int64 -> Integer) set(this, value) {
        this.value = value;
        return this;
    }

    fun (->int64) __main__() {
        Integer[] integer_array = new 10 of Integer(1);
        integer_array[4].value = 3;
        return integer_array[3].value * (integer_array[4].value == 3);
    }

}
