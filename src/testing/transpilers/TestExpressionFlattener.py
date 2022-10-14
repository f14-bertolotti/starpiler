import unittest

from src.semantics.slang import run
from src.semantics.slang import parsed
from src.semantics.slang import transformed
from src.semantics.slang import assembled
from src.transpilers import flattenExpression
from src.testing.slang import tests
import inspect


class TestExpressionFlattener(unittest.TestCase): pass

for testname in tests:
    def make():
        def f(self):
            self.assertEqual(run(program_tree=flattenExpression(parsed(tests[f.__name__[5:]]["program"]))), tests[f.__name__[5:]]["result"])
        f.__name__ = f"test_{testname}"
        return f
    setattr(TestExpressionFlattener, f"test_{testname}", make())

if __name__ == "__main__":
    unittest.main()


