from src.syntax import Production
from src.syntax import Rule

signedInteger = Production(name="wl_int", rules=[Rule("/[-+]?[0-9]+/")])
identifier = Production(name="wl_id", rules=[Rule("/[a-zA-z]+[a-zA-Z0-9]*/")])
