from src.syntax.slang import lang
from pathlib import Path

from llvmlite import ir
from lark.visitors import Transformer

import sys
import rich

rich.print(lang.parse(Path(sys.argv[1]).read_text()))

module = ir.Module( name="MainModule" )


