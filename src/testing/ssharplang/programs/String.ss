class String {

    var int8[] buffer;

    fun (String, int8[]->String) __init__(this, buffer) {
        this.buffer = buffer;
        return this;
    }

    fun (String -> int64) size(this) {
        int64 i = 0;
        while ( this.buffer[i] as int64 != 0 ) {
            i = i + 1;
        }
        return i;
    }

    fun (String -> String) clone(this) {
        int64 size = this.size() + 1;
        int8[] buffer = new size of int8;
        for i from size {
            buffer[i] = this.buffer[i];
        }
        buffer[size-1] = 0 as int8;
        return new String(buffer);
    }

    fun (String, String -> String) concat(this, other) {
        int64 size = this.size() + other.size() + 1;
        int8[] buffer = new size of int8;
        for i from this.size() {
            buffer[i] = this.buffer[i];
        }
        for i from other.size() {
            buffer[i + this.size()] = other.buffer[i];
        }
        buffer[size - 1] = 0 as int8;

        this.buffer = buffer;
        return this;
    }

    fun (String, String -> int64) equals(this, other) {
        if (this.size() != other.size()) {return 0;}
        for i from this.size() {
            if (this.buffer[i] as int64 != other.buffer[i] as int64) {return 0;}
        }
        return 1;
    }

    fun (String -> String) print(this) {
        print(this.buffer);
        return this;
    }

    fun (->int64) __main__() {
        String string1 = new String("Hello World!\n");
        String string2 = new String("Hello World!\n");
        String string3 = new String("Hello World!\nHello World!\n");
        string1.concat(string2);

        return string1.equals(string3);
    }

}
