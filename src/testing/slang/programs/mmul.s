
def int8* malloc(int64);
def void free(int8*);

def int64** newmatrix(int64 rows, int64 cols) does
    int64** matrix = &malloc(8 * rows) as int64**;
    int64 i = 0;
    while i < 3 do
        matrix&[i] = &malloc(8 * cols) as int64*;
        &i = i + 1;
    ;
    return matrix;
;

def int64 initAsIdentityMatrix(int64** m, int64 r, int64 c) does
    int64 i = 0;
    while i < r do
        int64 j = 0;
        while j < c do
            m[i]&[j] = i == j;
            &j = j + 1;
        ;
        &i = i + 1;
    ;
    return 0;
;

def int64** mmul(int64** m1, int64 r1, int64 c1, int64** m2, int64 r2, int64 c2) does
    int64** m = &newmatrix(r1, c2);
    int64 i = 0;
    while i < r1 do
        int64 j = 0;
        while j < c2 do
            int64 cum = 0;
            int64 k = 0;
            while k < c1 do
                &cum = cum + m1[i][k] * m2[k][j];
                &k = k + 1;
            ;
            m[i]&[j] = cum;
            &j = j + 1;
        ;
        &i = i + 1;
    ;
    return m;
;

def int64 freematrix(int64** matrix, int64 rows, int64 cols) does
    int64 i = 0;
    while i < 3 do
        &free(matrix[i] as int8*);
        &i = i + 1;
    ;
    &free(matrix as int8*);
    return 0;
;


def int64 start() does
    int64** m1 = &newmatrix(3,3);
    int64** m2 = &newmatrix(3,3);
    int64 res = &initAsIdentityMatrix(m1,3,3);
    int64 res = &initAsIdentityMatrix(m2,3,3);
    int64** m3 = &mmul(m1,3,3,m2,3,3);
    int64 result = m3[0][0] == 1 * 
                   m3[0][1] == 0 *
                   m3[0][2] == 0 *
                   m3[1][0] == 0 *
                   m3[1][1] == 1 *
                   m3[1][2] == 0 *
                   m3[2][0] == 0 *
                   m3[2][1] == 0 *
                   m3[2][2] == 1;
    int64 res = &freematrix(m1,3,3);
    int64 res = &freematrix(m2,3,3);
    int64 res = &freematrix(m3,3,3);
    return result;
;


