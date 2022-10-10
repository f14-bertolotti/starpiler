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
            int64 result = &increment(10);
            return result;
        ;
        """
        self.assertEqual(run(program), 11)

    def test_mutableVars(self):
        program = """
        def int64 start() does
            int64 x = 10;
            &x = 11;
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
        def double start() does
            return 100.0 / 10.0;
        ;
        """
        self.assertEqual(run(program), 10.0)

    def test_floatMultiplication(self):
        program = """
        def double start() does
            return 10.0 * 10.0;
        ;
        """
        self.assertEqual(run(program), 100.0)

    def test_subfloat(self):
        program = """
        def double start() does
            return (1.0 - 1.5);
        ;
        """
        self.assertEqual(run(program), -0.5)

    def test_cast1(self):
        program = """
        def double start() does
            return 1 as double;
        ;
        """
        self.assertEqual(run(program), 1.0)

    def test_negation(self):
        program = """
        def int64 start() does
            return -10;
        ;
        """
        self.assertEqual(run(program), -10)

    def test_floatNegation(self):
        program = """
        def double start() does
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
        def double start() does
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
        def double start() does
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
        def double start() does
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
        def double start() does
            return -10.0 * 10.0 / 2.0 + 10.0 * 10.0;
        ;
        """
        self.assertEqual(run(program), 50.0)

    def test_expression4(self):
        program = """
        def int64 start() does
            return 4.0 > (2 as double);
        ;
        """
        self.assertEqual(run(program), 1)

    def test_expression_gte1(self):
        program = """
        def int64 start() does
            return 4.0 >= (4 as double);
        ;
        """
        self.assertEqual(run(program), 1)
    
    def test_expression_gte2(self):
        program = """
        def int64 start() does
            return 4 >= 2;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_expression_lss1(self):
        program = """
        def int64 start() does
            return 4.0 < (4 as double);
        ;
        """
        self.assertEqual(run(program), 0)
    
    def test_expression_lss2(self):
        program = """
        def int64 start() does
            return 4 < 2;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_expression_leq1(self):
        program = """
        def int64 start() does
            return 4.0 <= (4 as double);
        ;
        """
        self.assertEqual(run(program), 1)
    
    def test_expression_leq2(self):
        program = """
        def int64 start() does
            return 4 <= 2;
        ;
        """
        self.assertEqual(run(program), 0)

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
            if x != y do &y = x;;
            return y;
        ;
        """
        self.assertEqual(run(program), 10)

    def test_ifthen7(self):
        program = """
        def int64 start() does
            int64 x = 5+5;
            int64 y = 4+5;
            if x != y do &y = y + 1;;
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
            while x != y do &y = x;;
            return y;
        ;
        """
        self.assertEqual(run(program), 10)

    def test_while2(self):
        program = """
        def int64 start() does
            int64 x = 10;
            int64 y = 5;
            while x != y do &y = y + 1;;
            return y;
        ;
        """
        self.assertEqual(run(program), 10)

    def test_while3(self):
        program = """
        def int64 start() does
            int64 x = 10;
            while x != 0 do
                &x = x - 1;
            ;
            return x;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_pointer1(self):
        program = """
        def int8* malloc(int64);
        def void free(int8*);

        def int64 start() does
            int64* x = &malloc(8 * 3) as int64*;
            x&[0] = 0;
            x&[1] = 0;
            x&[2] = 0;
            int64 a = x[0];
            int64 b = x[1];
            int64 c = x[2];
            &free(x as int8*);
            return a == b * b == c * c == 0;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_pointer2(self):
        program = """

        def int8* malloc(int64);
        def void free(int8*);

        def int64 start() does
            int64** x = &malloc(8 * 3) as int64**;
            x&[0] = &malloc(8 * 3) as int64*;
            x&[1] = &malloc(8 * 3) as int64*;
            x&[2] = &malloc(8 * 3) as int64*;
            x[0]&[0] = 0;
            x[0]&[1] = 1;
            x[0]&[2] = 2;
            x[1]&[0] = 3;
            x[1]&[1] = 4;
            x[1]&[2] = 5;
            x[2]&[0] = 6;
            x[2]&[1] = 7;
            x[2]&[2] = 8;
            int64 result = x[0][0] == 0 * 
                           x[0][1] == 1 * 
                           x[0][2] == 2 *
                           x[1][0] == 3 *
                           x[1][1] == 4 *
                           x[1][2] == 5 *
                           x[2][0] == 6 *
                           x[2][1] == 7 *
                           x[2][2] == 8;

            &free(x[0] as int8*);
            &free(x[1] as int8*);
            &free(x[2] as int8*);
            &free(x as int8*);

            return result;
        ;
        """ 
        self.assertEqual(run(program),1)

    def test_printf1(self):
        program = """
        def int32 printf(int8*, ...);
        def int8* malloc(int64);
        def void free(int8*);

        def int64 start() does
            int8* f = &malloc(3) as int8*;
            int8* s = &malloc(1) as int8*;
            s&[0] = 65 as int8;
            s&[1] = 65 as int8;
            s&[2] = 0 as int8;
            f&[0] = 0 as int8;
            &printf(f,s);
            &free(f);
            &free(s);
            return 0;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_printf2(self):
        program = """
        def int32 printf(int8*, ...);
        def int64 start() does
            &printf(\"%s\",\"\");
            return 0;
        ;
        """
        self.assertEqual(run(program), 0)

    def test_array1(self):
        program = """
        def int64 start() does
            int64* x = [1,2,3,4];
            int64** y = [[1,2,3],[1,2]];
            return x[0] == 1 * 
                   x[1] == 2 *
                   x[2] == 3 *
                   x[3] == 4 *
                   y[0][0] == 1 *
                   y[0][1] == 2 *
                   y[0][2] == 3 *
                   y[1][0] == 1 *
                   y[1][1] == 2;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_array2(self):
        program = """
        def int64 start() does
            int64* x = [1,2];
            int64** y = [x,x];
            return x[0] == 1 * 
                   x[1] == 2 *
                   y[0][0] == 1 *
                   y[0][1] == 2 *
                   y[1][0] == 1 *
                   y[1][1] == 2;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_array3(self):
        program = """

        def int8* malloc(int64);
        def void free(int8*);
        def int8* memcpy(int8*,int8*,int32); 

        def int64 start() does
            int64* x = [1,2,3,4,5];
            int64* y = &malloc(8 * 5) as int64*;
            &memcpy(y as int8*, x as int8*, (8 * 5) as int32);
            int64 result = y[0] == 1 * 
                           y[1] == 2 *
                           y[2] == 3 *
                           y[3] == 4 *
                           y[4] == 5;
            &free(y as int8*);
            return result;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_globalValue(self):
        program = """
        def int64 x = 0;
        def int64 y = 1;
        def int64* z = [x + y,2,3,4];
        def int64 start() does
            int64 result = x == 0 * y == 1 * 
                     z[0] == 1 *
                     z[1] == 2 *
                     z[2] == 3 *
                     z[3] == 4;
            return result;
        ;
        """
        self.assertEqual(run(program), 1)

    def test_import1(self):
        program = """
        from "src/programs/slang/Increment.sl" import increment as inc;
        from "src/programs/slang/Increment.sl" import x as y;

        def int64 start() does
            return &inc(y);
        ;
        """
        self.assertEqual(run(program),1)

    def test_import2(self):
        program = """
        from "src/programs/slang/DoubleDoubleIncrement.sl" import doubleDoubleIncrement as inc;

        def int64 start() does
            return &inc(0);
        ;
        """
        self.assertEqual(run(program), 4)

    def test_import3(self):
        program = """
        from "src/programs/slang/DoubleDoubleIncrement.sl" import doubleDoubleIncrement as inc;
        from "src/programs/slang/Shape2Sides.sl" import triangle as triangle;
        from "src/programs/slang/Shape2Sides.sl" import square as square;

        def int64 start() does
            return &inc(triangle + square);
        ;
        """
        self.assertEqual(run(program), 11)

    def test_ftype1(self):
        program = """
        def int64 increment(int64 x) does
            return x + 1;
        ;

        def int64 start() does
            int8* f = &increment as int8*;
            return (f as (int64 -> int64)*)(0);
        ;
        """
        self.assertEqual(run(program), 1)

    def test_extern1(self):

        program = """
        def int32 printf(int8*, ...);

        def int64 start() does
            &printf("%s","");
            return 0;
        ;
        """
        self.assertEqual(run(program),0)

    def test_comment(self):

        program = """
        def int64 start() does
            # A COMMENT
            return 0;
        ;
        """
        self.assertEqual(run(program),0)

    def test_program2string(self):
        program = """
        from "src/programs/slang/Increment.sl" import increment as increment;
        def int8* malloc(int8*);
        def int64 X = 1;
        def int64 start() does
            return &increment(X);
        ;
        """
        self.assertEqual(str(transformed(program)), "Module(Import(/home/f14/Devel/MetaTranspiler/src/programs/slang/Increment.sl,Name(increment),Name(increment)),FunctionDeclaration(FType(Int8*->Int8*),Name(malloc)),GlobalAssignement(Int64,Name(X),Integer(i64 1)),FunctionDefinition(Name(start),ParamSeqDef(),Block(Return(Call(Ref(Name(increment)),Name(X))))))")

    def test_program2string_cast(self):
        program = """
        def double start() does return 0 as double;;
        """
        self.assertEqual(str(transformed(program)), "Module(FunctionDefinition(Name(start),ParamSeqDef(),Block(Return(Cast(Double,Integer(i64 0))))))")


    def test_program2string_array(self):
        program = """
        def int64* array = [0,1,2,3,4];
        def int64 start() does return array[0];;
        """
        self.assertEqual(str(transformed(program)), "Module(GlobalAssignement(Int64*,Name(array),Array(Integer(i64 0),Integer(i64 1),Integer(i64 2),Integer(i64 3),Integer(i64 4))),FunctionDefinition(Name(start),ParamSeqDef(),Block(Return(Name(array)[[Integer(i64 0)]]))))")

    def test_program2string_binary_op(self):
        program = """
        def int64 start() does return 1 + 1;;
        """
        self.assertEqual(str(transformed(program)), "Module(FunctionDefinition(Name(start),ParamSeqDef(),Block(Return(Add(Integer(i64 1),Integer(i64 1))))))")

    def test_program2string_unary_op(self):
        program = """
        def int64 start() does return -1;;
        """
        self.assertEqual(str(transformed(program)), "Module(FunctionDefinition(Name(start),ParamSeqDef(),Block(Return(Neg(Integer(i64 1))))))")

    def test_program2string_params(self):
        program = """def int64 f(int64 x, int64 y, int64 z) does return 0;;
                     def int64 start() does return f(0);;"""
        self.assertEqual(str(transformed(program)), "Module(FunctionDefinition(Name(f),ParamSeqDef(Parameter(Int64,Name(x)),Parameter(Int64,Name(y)),Parameter(Int64,Name(z))),Block(Return(Integer(i64 0)))),FunctionDefinition(Name(start),ParamSeqDef(),Block(Return(Call(Name(f),Integer(i64 0))))))")

    def test_raise_operation_not_found(self):
        program_add = """def int64 start() does return "aaa" + "bbb";;"""
        program_mul = """def int64 start() does return "aaa" * "bbb";;"""
        program_sub = """def int64 start() does return "aaa" - "bbb";;"""
        program_div = """def int64 start() does return "aaa" / "bbb";;"""
        program_mod = """def int64 start() does return "aaa" % "bbb";;"""
        program_lss = """def int64 start() does return "aaa" < "bbb";;"""
        program_gtr = """def int64 start() does return "aaa" > "bbb";;"""
        program_lse = """def int64 start() does return "aaa" <= "bb";;"""
        program_gte = """def int64 start() does return "aaa" >= "bb";;"""
        program_eqs = """def int64 start() does return "aaa" == "bb";;"""
        program_neq = """def int64 start() does return "aaa" != "bb";;"""
        program_neg = """def int64 start() does return -"aaa";;"""
        with self.assertRaises(ValueError): assembled(program_add)
        with self.assertRaises(ValueError): assembled(program_mul)
        with self.assertRaises(ValueError): assembled(program_sub)
        with self.assertRaises(ValueError): assembled(program_div)
        with self.assertRaises(ValueError): assembled(program_mod)
        with self.assertRaises(ValueError): assembled(program_lss)
        with self.assertRaises(ValueError): assembled(program_gtr)
        with self.assertRaises(ValueError): assembled(program_lse)
        with self.assertRaises(ValueError): assembled(program_gte)
        with self.assertRaises(ValueError): assembled(program_eqs)
        with self.assertRaises(ValueError): assembled(program_neq)
        with self.assertRaises(ValueError): assembled(program_neg)

    def test_raise_non_coherent_types(self):
        program_add = """def int64 start() does return 1.0 + 1;;"""
        with self.assertRaises(ValueError): assembled(program_add)
        
    def test_variable_declaration2(self):
        program = """
        def int64 x;
        def int64 start() does
            &x = 1;
            return x;
        ;
        """
        self.assertEqual(run(program), 1)

if __name__ == "__main__":
    unittest.main()

