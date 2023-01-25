class Integer {
    
    var int64 value;

    fun (Integer, int64 -> Integer) __init__ (this, value) {
        this.value = value;
        return this;
    }

}
