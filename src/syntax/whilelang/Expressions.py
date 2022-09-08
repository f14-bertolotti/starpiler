from src.syntax import Production
from src.syntax import Language
from src.syntax import Rule

from src.syntax.whilelang import identifier, signedInteger

expression     = Production(name="expr")
addition       = Production(name = "add" , rules = [Rule(expression, "\"+\"" , expression)])
subtraction    = Production(name = "sub" , rules = [Rule(expression, "\"-\"" , expression)])
multiplication = Production(name = "mul" , rules = [Rule(expression, "\"*\"" , expression)])
division       = Production(name = "div" , rules = [Rule(expression, "\"/\"" , expression)])
equality       = Production(name = "eq"  , rules = [Rule(expression, "\"==\"", expression)])
inquality      = Production(name = "neq" , rules = [Rule(expression, "\"!=\"", expression)])
expression.append(addition) \
          .append(subtraction) \
          .append(multiplication) \
          .append(division) \
          .append(equality) \
          .append(inquality) \
          .append(signedInteger) \
          .append(identifier)

