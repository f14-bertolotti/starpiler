from src.syntax import Language as L
from src.syntax import Production as P
from src.syntax import Rule as R

from src.syntax.slang import function, globalAssignement

from lark import Lark


globalValues = P(name = "slang_globals", rules = [function, globalAssignement], mod="?")
lang = Lark(L(P(name = "start", rules=[R(globalValues, mod="*")])).toLark(), keep_all_tokens=True)



