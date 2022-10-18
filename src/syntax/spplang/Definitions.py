from src.syntax.slang import functionDefinition as slangFunction
from src.syntax.slang import functionDeclaration as slangFunctionDeclaration
from src.syntax.slang import globalDeclaration 
from src.syntax.spplang import declarationAssignement, identifier, native, expression, statement, block

from src.syntax import Production as P
from src.syntax import Rule as R
from src.syntax import Terminal as T

from src.syntax import getFindAndReplaceVisitor
from src.syntax import getChangePrefixVisitor
from src.syntax import getClonerVisitor

methodDefinition = slangFunction.visit(getClonerVisitor(slangFunction)) \
                                .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                                .visit(getFindAndReplaceVisitor("slang_identifier" , identifier)) \
                                .visit(getFindAndReplaceVisitor("slang_block"      , block)) \
                                .visit(getChangePrefixVisitor  ("slang_"           , "spplang_"))

fieldDefinition = globalDeclaration.visit(getClonerVisitor(globalDeclaration)) \
                                   .visit(getFindAndReplaceVisitor("slang_type"                   , native)) \
                                   .visit(getFindAndReplaceVisitor("slang_identifier"             , identifier)) \
                                   .visit(getFindAndReplaceVisitor("slang_expression"             , expression)) \
                                   .visit(getFindAndReplaceVisitor("slang_declaration_assignment" , declarationAssignement)) \
                                   .visit(getChangePrefixVisitor  ("slang_"                       , "spplang_")) \
                                   .visit(getChangePrefixVisitor  ("spplang_global_assignement"   , "spplang_class_assignement"))

fieldDeclaration = P(name="spplang_field_declaration", rules = [R(T("def"), native, identifier, T(";"))])

definition = P(name="spplang_definition", rules=[methodDefinition, fieldDeclaration], mod="?")
                                     
classDefinition = P(name="spplang_class", rules=[R(T("class"), identifier, T("with"), R(definition, mod="*"), T(";"))])

functionDefinition = methodDefinition
functionDeclaration = slangFunctionDeclaration.visit(getClonerVisitor(slangFunctionDeclaration)) \
                                              .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                                              .visit(getFindAndReplaceVisitor("slang_identifier" , identifier)) \
                                              .visit(getChangePrefixVisitor  ("slang_"           , "spplang_"))

variableDefinition = fieldDefinition
