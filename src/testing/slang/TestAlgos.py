import unittest

from src.semantics.slang import run
from src.semantics.slang import parsed
from src.semantics.slang import transformed
from src.semantics.slang import assembled

class TestAlgos(unittest.TestCase):

    def test_bubblesort(self):
        program = """
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
            int64* array = malloc(8 * 5) as int64*;
            array&[0] = 4;
            array&[1] = 2;
            array&[2] = 1;
            array&[3] = 0;
            array&[4] = 3;
            int64 res = sort(array, 5);

            int64 sorted = array[0] == 0 *
                           array[1] == 1 *
                           array[2] == 2 *
                           array[3] == 3 *
                           array[4] == 4;
            free(array as int8*);
            return sorted;
        ;
        """
        self.assertEqual(run(program),1)

    def test_mmul(self):
        program = """

        def int64** newmatrix(int64 rows, int64 cols) does
            int64** matrix = malloc(8 * rows) as int64**;
            int64 i = 0;
            while i < 3 do
                matrix&[i] = malloc(8 * cols) as int64*;
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
            int64** m = newmatrix(r1, c2);
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
                free(matrix[i] as int8*);
                &i = i + 1;
            ;
            free(matrix as int8*);
            return 0;
        ;


        def int64 start() does
            int64** m1 = newmatrix(3,3);
            int64** m2 = newmatrix(3,3);
            int64 res = initAsIdentityMatrix(m1,3,3);
            int64 res = initAsIdentityMatrix(m2,3,3);
            int64** m3 = mmul(m1,3,3,m2,3,3);
            int64 result = m3[0][0] == 1 * 
                           m3[0][1] == 0 *
                           m3[0][2] == 0 *
                           m3[1][0] == 0 *
                           m3[1][1] == 1 *
                           m3[1][2] == 0 *
                           m3[2][0] == 0 *
                           m3[2][1] == 0 *
                           m3[2][2] == 1;
            int64 res = freematrix(m1,3,3);
            int64 res = freematrix(m2,3,3);
            int64 res = freematrix(m3,3,3);
            return result;
        ;

        """
        self.assertEqual(run(program),1)


    def test_dfs(self):
        program = """
        
        def int8** n0 = [[10] as int8*, 0  as int8*, 0  as int8*];
        def int8** n1 = [[9 ] as int8*, 0  as int8*, 0  as int8*];
        def int8** n2 = [[8 ] as int8*, n0 as int8*, n1 as int8*];

        def int8** n3 = [[7 ] as int8*, 0  as int8*, 0  as int8*];
        def int8** n4 = [[6 ] as int8*, 0  as int8*, 0  as int8*];
        def int8** n5 = [[5 ] as int8*, n3 as int8*, n4 as int8*];

        def int8** n6 = [[4 ] as int8*, n2 as int8*, n5 as int8*];

        def int64* res = [0,0,0,0,0,0,0];

        def int64 visit(int8** node, int64 i) does
            if (node as int64) == 0 do return i-1;;

            res&[i] = (node[0] as int64*)[0];

            &i = visit(node[1] as int8**, i + 1);
            &i = visit(node[2] as int8**, i + 1);

            return i;
        ;

        def int64 start() does
            visit(n6,0); 
            return res[0] == 4  *
                   res[1] == 8  *
                   res[2] == 10 *
                   res[3] == 9  *
                   res[4] == 5  *
                   res[5] == 7  *
                   res[6] == 6;
        ;
        """
        self.assertEqual(run(program), 1)




if __name__ == "__main__":
    unittest.main()

