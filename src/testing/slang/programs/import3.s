
from "src/testing/slang/programs/DoubleDoubleIncrement.s" import doubleDoubleIncrement as inc;
from "src/testing/slang/programs/Shape2Sides.s" import triangle as triangle;
from "src/testing/slang/programs/Shape2Sides.s" import square as square;

def int64 start() does
    return &inc(triangle + square);
;
