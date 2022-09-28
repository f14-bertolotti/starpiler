import unittest

from src.semantics.slang import run
from src.semantics.slang import parsed
from src.semantics.slang import transformed
from src.semantics.slang import assembled

class TestAlgos(unittest.TestCase):

    def test_bublesort(self):
        program = """
        def int64 sort(int64* array, int64 len) does
            int64 i = 0;
            while i < len do
                int64 j = i;
                while j < len do
                    if array[i] > array[j] do
                        int64 tmp = array[i];
                        array[i] = array[j];
                        array[j] = tmp;
                    ;
                    j = j + 1;
                ;   
                i = i + 1;
            ;
            return 0;
        ;

        def int64 start() does
            int64* array = (int64*) malloc(8 * 5);
            array[0] = 4;
            array[1] = 2;
            array[2] = 1;
            array[3] = 0;
            array[4] = 3;
            int64 res = sort(array, 5);

            int64 sorted = array[0] == 0 *
                           array[1] == 1 *
                           array[2] == 2 *
                           array[3] == 3 *
                           array[4] == 4;
            free((int8*) array);
            return sorted;
        ;
        """
        self.assertEqual(run(program),1)

    def test_matrix(self):
        program = """
        def int64 start() does
            int64** matrix = (int64**) malloc(8 * 5);

            int64 i = 0;
            while i < 5 do
                matrix[i] = (int64*) malloc(8 * 5);
                i = i + 1;
            ;

            matrix[0][0] = 1;

            i = 0;
            while i < 5 do
                free((int8*) matrix[i]);
                i = i + 1;
            ;

            free((int8*) matrix);

            return 0;
        ;

        """

        print(run(program))



if __name__ == "__main__":
    unittest.main()

