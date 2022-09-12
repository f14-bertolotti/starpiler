from src.syntax import Production
from src.syntax import Rule

signedInteger = Production(name="int", rules=[Rule("/[-+]?[0-9]+/")])
identifier = Production(name="id", rules=[Rule("/[a-zA-z]+[a-zA-Z0-9]*/")])
