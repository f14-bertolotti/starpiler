import unittest

from src.semantics.slang import run
from src.semantics.slang import transformed
from src.semantics.slang import assembled
from src.testing.slang import tests
from pathlib import Path


class TestBasics(unittest.TestCase):

    def test_program2string(self):
        program = """
        from "src/testing/slang/programs/Increment.s" import increment as increment;
        def int8* malloc(int8*);
        def int64 X = 1;
        def int64 start() does
            return &increment(X);
        ;
        """
        self.assertEqual(str(transformed(program)), "Module(Import(/home/f14/Devel/MetaTranspiler/src/testing/slang/programs/Increment.s,Name(increment),Name(increment)),FunctionDeclaration(FType((Int8)*->(Int8)*),Name(malloc)),GlobalAssignement(Int64,Name(X),Integer(i64 1)),FunctionDefinition(Name(start),ParamSeqDef(),Block(Return(Call(Ref(Name(increment)),Name(X))))))")

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
        self.assertEqual(str(transformed(program)), "Module(GlobalAssignement((Int64)*,Name(array),Array(Integer(i64 0),Integer(i64 1),Integer(i64 2),Integer(i64 3),Integer(i64 4))),FunctionDefinition(Name(start),ParamSeqDef(),Block(Return(Index(Name(array),[Integer(i64 0)])))))")

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
        

for testname in tests:
    def make():
        def f(self):
            self.assertEqual(run(program_string=Path(tests[f.__name__[5:]]["path"]).read_text()), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(TestBasics, f"test_{testname}", make())

if __name__ == "__main__":
    unittest.main()

