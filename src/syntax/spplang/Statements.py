from src.syntax.slang import statement as slangStatement
from src.syntax.spplang import expression, native, identifier

from src.syntax import getFindAndReplaceVisitor
from src.syntax import getChangePrefixVisitor
from src.syntax import getClonerVisitor

statement = slangStatement.visit(getClonerVisitor(slangStatement)) \
                          .visit(getFindAndReplaceVisitor("slang_expression", expression)) \
                          .visit(getFindAndReplaceVisitor("slang_type", native)) \
                          .visit(getFindAndReplaceVisitor("slang_identifier", identifier)) \
                          .visit(getChangePrefixVisitor("slang_","spplang_"))

if __name__ == "__main__":
    from src.syntax import Language 
    print(Language(statement).toLark())
