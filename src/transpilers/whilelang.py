from src.syntax.whilelang import whilelang
from src.semantics.whilelang.c import Transpiler
from pathlib import Path
import sys

print(whilelang.source_grammar)
print()
parsed = whilelang.parse(Path(sys.argv[1]).read_text())
print(parsed)
print()
print(Transpiler(visit_tokens=True).transform(parsed))
 






