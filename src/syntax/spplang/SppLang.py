from src.syntax import Language as L
from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.spplang import classDefinition, functionDefinition, functionDeclaration, variableDefinition, identifier, string

from lark import Lark


imports = P(name = "spplang_import", rules = [R(T("from"), string, T("import"), identifier, T("as"), identifier, T(";"))])

globalDefinition = P(name = "spplang_globals", rules = [functionDeclaration, classDefinition, functionDefinition, variableDefinition], mod="?")

lang = Lark(L(P(name = "spplang_start", rules=[R(R(imports, mod="*"), R(globalDefinition, mod="*"))])).toLark(), keep_all_tokens=True, propagate_positions=True)

