from src.syntax import Production
from src.syntax import Language
from src.syntax import Rule

from src.syntax.whilelang import identifier, signedInteger

expression     = Production(name = "wl_expr")
addition       = Production(name = "wl_add" , rules = [Rule(expression, "\"+\"" , expression)])
subtraction    = Production(name = "wl_sub" , rules = [Rule(expression, "\"-\"" , expression)])
multiplication = Production(name = "wl_mul" , rules = [Rule(expression, "\"*\"" , expression)])
division       = Production(name = "wl_div" , rules = [Rule(expression, "\"/\"" , expression)])
equality       = Production(name = "wl_eq"  , rules = [Rule(expression, "\"==\"", expression)])
inquality      = Production(name = "wl_neq" , rules = [Rule(expression, "\"!=\"", expression)])
expression.append(addition) \
          .append(subtraction) \
          .append(multiplication) \
          .append(division) \
          .append(equality) \
          .append(inquality) \
          .append(signedInteger) \
          .append(identifier)

