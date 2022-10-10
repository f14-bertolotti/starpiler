from src.syntax.slang import functionDefinition as slangFunction
from src.syntax.slang import globalAssignement 
from src.syntax.spplang import declarationAssignement, identifier, native, expression, statement, block

from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax import getFindAndReplaceVisitor
from src.syntax import getChangePrefixVisitor
from src.syntax import getClonerVisitor

functionDefinition = slangFunction.visit(getClonerVisitor(slangFunction)) \
                                  .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                                  .visit(getFindAndReplaceVisitor("slang_identifier" , identifier)) \
                                  .visit(getFindAndReplaceVisitor("slang_block"      , block)) \
                                  .visit(getChangePrefixVisitor  ("slang_"           , "spplang_"))

variableDefinition = globalAssignement.visit(getClonerVisitor(globalAssignement)) \
                                      .visit(getFindAndReplaceVisitor("slang_type"                    , native)) \
                                      .visit(getFindAndReplaceVisitor("slang_identifier"              , identifier)) \
                                      .visit(getFindAndReplaceVisitor("slang_expression"              , expression)) \
                                      .visit(getFindAndReplaceVisitor("slang_declaration_assignment" , declarationAssignement)) \
                                      .visit(getChangePrefixVisitor  ("slang_"                        , "spplang_"))

definition = P(name="spplang_definition", rules=[functionDefinition, variableDefinition], mod="?")
                                     
classDefinition = P(name="spplang_class", rules=[R(T("class"), identifier, T("with"), R(definition, mod="*"), T(";"))])

