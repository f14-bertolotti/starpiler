from src.syntax import Language as L
from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax.ssharplang import classDefinition, identifier, string

from src.utils import SMLark


imports = P(name = "ssharplang_import", rules = [R(T("from"), string, T("import"), identifier, T("as"), identifier, T(";"))])

lang = SMLark(L(P(name = "ssharplang_start", rules=[R(R(imports, mod="*"), classDefinition)])).toLark(), keep_all_tokens=True, propagate_positions=True)
