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
from src.syntax import getMatchesVisitor

methodDefinition = slangFunction.visit(getClonerVisitor(slangFunction)) \
                                .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                                .visit(getFindAndReplaceVisitor("slang_identifier" , identifier)) \
                                .visit(getFindAndReplaceVisitor("slang_block"      , block)) \
                                .visit(getChangePrefixVisitor  ("slang_"           , "spplang_"))
methodDefinition.name = "spplang_method_definition"

fieldDefinition = globalDeclaration.visit(getClonerVisitor(globalDeclaration)) \
                                   .visit(getFindAndReplaceVisitor("slang_type"                   , native)) \
                                   .visit(getFindAndReplaceVisitor("slang_identifier"             , identifier)) \
                                   .visit(getFindAndReplaceVisitor("slang_expression"             , expression)) \
                                   .visit(getFindAndReplaceVisitor("slang_declaration_assignment" , declarationAssignement)) \
                                   .visit(getChangePrefixVisitor  ("slang_"                       , "spplang_")) \
                                   .visit(getChangePrefixVisitor  ("spplang_global_assignement"   , "spplang_class_assignement"))

fieldDeclaration = P(name="spplang_field_declaration", rules = [R(T("def"), native, identifier, T(";"))])
fieldDefinition  = P(name="spplang_field_definition" , rules = [R(T("def"), native, identifier, T("="), expression, T(";"))])

definition = P(name="spplang_definition", rules=[methodDefinition, fieldDeclaration, fieldDefinition], mod="?")
                                     
classDefinition = P(name="spplang_class", rules=[R(T("class"), identifier, T("with"), R(definition, mod="*"), T(";"))])

functionDefinition = P(name = "spplang_function_definition", 
                       rules = [R(T("def"), 
                                  native, 
                                  identifier, 
                                  methodDefinition.visit(getMatchesVisitor(lambda x:isinstance(x,P) and x.name == "spplang_parameter_seq_def"))[0], 
                                  T("does"),
                                  block,
                                  T(";"))])
functionDeclaration = slangFunctionDeclaration.visit(getClonerVisitor(slangFunctionDeclaration)) \
                                              .visit(getFindAndReplaceVisitor("slang_type"       , native)) \
                                              .visit(getFindAndReplaceVisitor("slang_identifier" , identifier)) \
                                              .visit(getChangePrefixVisitor  ("slang_"           , "spplang_"))

variableDefinition = P(name="spplang_global_assignement" , rules = [R(T("def"), native, identifier, T("="), expression, T(";"))])
