from src.syntax.whilelang import statement
from src.syntax import Language, Production

program = Language(Production(name="start", rules=[statement]))
print(program.toLark())
