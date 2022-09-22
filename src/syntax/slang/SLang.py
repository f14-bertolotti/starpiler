from src.syntax import Language as L
from src.syntax import Production as P
from src.syntax import Rule as R

from src.syntax.slang import function

from lark import Lark

lang = Lark(L(P(name = "start", rules=[R(function, mod="*")])).toLark(), keep_all_tokens=True)



