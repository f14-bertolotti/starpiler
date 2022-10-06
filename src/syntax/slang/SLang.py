from src.syntax import Language as L
from src.syntax import Production as P
from src.syntax import Terminal as T
from src.syntax import Rule as R


from src.syntax.slang import functionDefinition, functionDeclaration, identifier, globalAssignement, string

from lark import Lark

importCommand = P(name = "slang_import", rules = [R(T("from"), string, T("import"), identifier, T("as"), identifier, T(";"))])
globalValues = P(name = "slang_globals", rules = [functionDefinition, functionDeclaration, importCommand, globalAssignement], mod="?")
lang = Lark(L(P(name = "start", rules=[R(globalValues, mod="*")])).toLark(), keep_all_tokens=True)



