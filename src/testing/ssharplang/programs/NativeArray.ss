
class NativeArray {

    fun (NativeArray->NativeArray) __init__(this) {
        return this;
    }

    fun (->int64) __main__() {

        in64[] array = new 100 of int64;
        for i from 100 { array[i] = 0; } 

        return array[0] == 0 * 
               array[99] == 0; 
    }

}
