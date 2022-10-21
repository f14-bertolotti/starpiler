
def int8* malloc(int64);
def void free(int8*);

def int64 sort(int64* array, int64 len) does
    int64 i = 0;
    while i < len do
        int64 j = i;
        while j < len do
            if array[i] > array[j] do
                int64 tmp = array[i];
                array&[i] = array[j];
                array&[j] = tmp;
            ;
            &j = j + 1;
        ;   
        &i = i + 1;
    ;
    return 0;
;

def int64 start() does
    int64* array = &malloc(8 * 5) as int64*;
    array&[0] = 4;
    array&[1] = 2;
    array&[2] = 1;
    array&[3] = 0;
    array&[4] = 3;
    int64 res = &sort(array, 5);

    int64 sorted = array[0] == 0 *
                   array[1] == 1 *
                   array[2] == 2 *
                   array[3] == 3 *
                   array[4] == 4;
    &free(array as int8*);
    return sorted;
;
 
