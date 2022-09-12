from src.syntax.whilelang import statement
from src.syntax import Language, Production
from lark import Lark

whilelang= Lark(Language(Production(name="start", rules=[statement])).toLark())
