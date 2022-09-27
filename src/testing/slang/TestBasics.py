import unittest

from src.semantics.slang import run
from src.semantics.slang import parsed
from src.semantics.slang import transformed
from src.semantics.slang import assembled

class TestBasics(unittest.TestCase):

    def test_increment(self):
        program = """
        def int64 increment(int64 x) does
           return x + 1;
        ;
        
        def int64 start() does
            int64 result = increment(10);
            return result;
        ;
        """
        self.assertEqual(run(program), 11)

    def test_mutableVars(self):
        program = """
        def int64 start() does
            int64 x = 10;
            x = 11;
            return x;
        ;
        """
        self.assertEqual(run(program), 11)

    def test_multiplication(self):
        program = """
        def int64 start() does
            return 10 * 10;
        ;
        """
        self.assertEqual(run(program), 100)

    def test_division(self):
        program = """
        def int64 start() does
            return 100 / 10;
        ;
        """
        self.assertEqual(run(program), 10)

    def test_floatDivision(self):
        program = """
        def float64 start() does
            return 100.0 / 10.0;
        ;
        """
        self.assertEqual(run(program), 10.0)

    def test_floatMultiplication(self):
        program = """
        def float64 start() does
            return 10.0 * 10.0;
        ;
        """
        self.assertEqual(run(program), 100.0)

    def test_negation(self):
        program = """
        def int64 start() does
            return -10;
        ;
        """
        self.assertEqual(run(program), -10)

    def test_floatNegation(self):
        program = """
        def float64 start() does
            return -10.0;
        ;
        """
        self.assertEqual(run(program), -10.0)

    def test_modulo(self):
        program = """
        def int64 start() does
            return 10 % 4;
        ;
        """
        self.assertEqual(run(program),2)

    def test_floatModulo(self):
        program = """
        def float64 start() does
            return 10.0 % 4.0;
        ;
        """
        self.assertEqual(run(program),2.0)

    def test_equality(self):
        program = """
        def int64 start() does
            return 10 == 10;
        ;
        """
        self.assertEqual(run(program), 1)
        program = """
        def int64 start() does
            return 10 == 0;
        ;
        """
        self.assertEqual(run(program), 0)
 
    def test_floatEquality(self):
        program = """
        def int64 start() does
            return 10.0 == 10.0;
        ;
        """
        self.assertEqual(run(program), 1)
        program = """
        def int64 start() does
            return 10.0 == 0.0;
        ;
        """
        self.assertEqual(run(program), 0)
 
    def test_nequality(self):
        program = """
        def int64 start() does
            return 10 != 10;
        ;
        """
        self.assertEqual(run(program), 0)
        program = """
        def int64 start() does
            return 10 != 0;
        ;
        """
        self.assertEqual(run(program), 1)
 
    def test_floatNequality(self):
        program = """
        def int64 start() does
            return 10.0 != 10.0;
        ;
        """
        self.assertEqual(run(program), 0)
        program = """
        def int64 start() does
            return 10.0 != 0.0;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_expression1(self):
        program = """
        def int64 start() does
            return -10 * 10 + 10;
        ;
        """
        self.assertEqual(run(program), -90)

    def test_expression1F(self):
        program = """
        def float64 start() does
            return -10.0 * 10.0 + 10.0;
        ;
        """
        self.assertEqual(run(program), -90.0)

    def test_expression2(self):
        program = """
        def int64 start() does
            return -10 * 10 + 10 * 10;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_expression2F(self):
        program = """
        def float64 start() does
            return -10.0 * 10.0 + 10.0 * 10.0;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_expression3(self):
        program = """
        def int64 start() does
            return -10 * 10 / 2 + 10 * 10;
        ;
        """
        self.assertEqual(run(program), 50)

    def test_expression3F(self):
        program = """
        def float64 start() does
            return -10.0 * 10.0 / 2.0 + 10.0 * 10.0;
        ;
        """
        self.assertEqual(run(program), 50.0)

    def test_ifthen1(self):
        program = """
        def int64 start() does
            if 1 == 1 do return 1;;
            return 0;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_ifthen2(self):
        program = """
        def int64 start() does
            if 0 == 1 do return 1;;
            return 0;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_ifthen3(self):
        program = """
        def int64 start() does
            if 1 == 1 do 
                if 2 == 2 do 
                    return 2;
                ;
                return 1;
            ;
            return 0;
        ;
        """
        self.assertEqual(run(program), 2)

    def test_ifthen4(self):
        program = """
        def int64 start() does
            if 1 == 1 do 
                if 2 == 1 do 
                    return 2;
                ;
                return 1;
            ;
            return 0;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_ifthen5(self):
        program = """
        def int64 start() does
            if 1 == 0 do return 1;;
            if 2 == 0 do return 2;;
            if 3 == 0 do return 3;;
            return 0;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_ifthen6(self):
        program = """
        def int64 start() does
            if 1 == 0 do return 1;;
            if 2 == 2 do return 2;;
            if 3 == 0 do return 3;;
            return 0;
        ;
        """
        self.assertEqual(run(program), 2)

    def test_ifthen6(self):
        program = """
        def int64 start() does
            int64 x = 10;
            int64 y = 9;
            if x != y do y = x;;
            return y;
        ;
        """
        self.assertEqual(run(program), 10)

    def test_ifthen7(self):
        program = """
        def int64 start() does
            int64 x = 5+5;
            int64 y = 4+5;
            if x != y do y = y + 1;;
            return y;
        ;
        """
        self.assertEqual(run(program), 10)

    def test_ifthen8(self):
        program = """
        def int64 start() does
            int64 x = 10;
            int64 y = 5;
            if x != y do int64 y = y + 1;;
            return y;
        ;
        """
        self.assertEqual(run(program), 5)


    def test_while1(self):
        program = """
        def int64 start() does
            int64 x = 10;
            int64 y = 9;
            while x != y do y = x;;
            return y;
        ;
        """
        self.assertEqual(run(program), 10)

    def test_while2(self):
        program = """
        def int64 start() does
            int64 x = 10;
            int64 y = 5;
            while x != y do y = y + 1;;
            return y;
        ;
        """
        self.assertEqual(run(program), 10)

    def test_while3(self):
        program = """
        def int64 start() does
            int64 x = 10;
            while x != 0 do
                x = x - 1;
            ;
            return x;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_pointer1(self):
        program = """
        def int64 start() does
            int64* x = (int64*) malloc(8 * 3);
            x[0] = 0;
            x[1] = 0;
            x[2] = 0;
            int64 a = x[0];
            int64 b = x[1];
            int64 c = x[2];
            free((int8*) x);
            return a == b * b == c;
        ;
        """
        self.assertEqual(run(program), 1)


if __name__ == "__main__":
    unittest.main()

