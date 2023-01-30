from lark import Tree, Token
from src.semantics.types import *

importMalloc = \
Tree(Token('RULE', 'spplang_import'), [
    Token('FROM', 'from'), 
    Tree(Token('RULE', 'spplang_string'), [Token('__ANON__', '"src/testing/spplang/programs/gc/GC.spp"')]), 
    Token('IMPORT', 'import'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'malloc')]), 
    Token('AS', 'as'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__malloc__')]), 
    Token('SEMICOLON', ';')])

importMemcpy = \
Tree(Token('RULE', 'spplang_import'), [
    Token('FROM', 'from'), 
    Tree(Token('RULE', 'spplang_string'), [Token('__ANON__', '"src/testing/spplang/programs/gc/GC.spp"')]), 
    Token('IMPORT', 'import'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'memcpy')]), 
    Token('AS', 'as'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__memcpy__')]), 
    Token('SEMICOLON', ';')])


importMemcpyn = \
Tree(Token('RULE', 'spplang_import'), [
    Token('FROM', 'from'), 
    Tree(Token('RULE', 'spplang_string'), [Token('__ANON__', '"src/testing/spplang/programs/gc/GC.spp"')]), 
    Token('IMPORT', 'import'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'memcpyn')]), 
    Token('AS', 'as'), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__memcpyn__')]), 
    Token('SEMICOLON', ';')])

importGC = \
Tree(Token("RULE", "spplang_import"), [
    Token("FROM", "from"), 
    Tree(Token("RULE", "spplang_string"), [Token("__ANON__", "\"src/testing/spplang/programs/gc/GC.spp\"")]), 
    Token("IMPORT", "import"), 
    Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "GC")]), 
    Token("AS", "as"), 
    Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "GC")]), 
    Token("SEMICOLON", ";")])

importgc = \
Tree(Token("RULE", "spplang_import"), [
    Token("FROM", "from"), 
    Tree(Token("RULE", "spplang_string"), [Token("__ANON__", "\"src/testing/spplang/programs/gc/GC.spp\"")]), 
    Token("IMPORT", "import"), 
    Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "gc")]), 
    Token("AS", "as"), 
    Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "gc")]), 
    Token("SEMICOLON", ";")])

gcPop = \
Tree(Token('RULE', 'ssharplang_stmt_expr'), [
    Tree(Token('RULE', 'ssharplang_function_call'), [
        Tree(Token('RULE', 'ssharplang_struct_access'), [
            Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'gc')]), 
            Token('DOT', '.'), 
            Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'pop')])]), 
        Token('LPAR', '('), 
        Token('RPAR', ')')]), 
    Token('SEMICOLON', ';')])

sppMainMethod = \
Tree(Token('RULE', 'ssharplang_function_definition'), [
    Token('DEF', 'def'), 
    Tree(Token('RULE', 'ssharplang_int64'), [Token('INT64', 'int64')]), 
    Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'start')]), 
    Tree(Token('RULE', 'ssharplang_parameter_seq_def'), [Token('LPAR', '('), Token('RPAR', ')')]), 
    Token('DOES', 'does'), 
    Tree(Token('RULE', 'ssharplang_block'), [
        Tree(Token('RULE', 'ssharplang_stmt_expr'), [
            Tree(Token('RULE', 'ssharplang_assignement'), [
                Tree(Token('RULE', 'ssharplang_reference'), [
                    Token('AMPERSAND', '&'), 
                    Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'gc')])]), 
                Token('EQUAL', '='), 
                Tree(Token('RULE', 'ssharplang_new'), [
                    Token('NEW', 'new'), 
                    Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'GC')]), 
                    Token('LPAR', '('), 
                    Token('RPAR', ')')])]), 
            Token('SEMICOLON', ';')]),]), 
    Token('SEMICOLON', ';')])

gcEnd = \
Tree(Token('RULE', 'ssharplang_stmt_expr'), [
    Tree(Token('RULE', 'ssharplang_function_call'), [
        Tree(Token('RULE', 'ssharplang_struct_access'), [
            Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'gc')]), 
            Token('DOT', '.'), 
            Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'end')])]), 
        Token('LPAR', '('), 
        Token('RPAR', ')')]), 
    Token('SEMICOLON', ';')])



gcMarkAndSweep = \
Tree(Token('RULE', 'ssharplang_stmt_expr'), [
    Tree(Token('RULE', 'ssharplang_function_call'), [
        Tree(Token('RULE', 'ssharplang_struct_access'), [
            Tree(Token('RULE', 'ssharplang_function_call'), [
                Tree(Token('RULE', 'ssharplang_struct_access'), [
                    Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'gc')]), 
                    Token('DOT', '.'), 
                    Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'mark')])]), 
                Token('LPAR', '('), Token('RPAR', ')')]), 
            Token('DOT', '.'), 
            Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', 'sweep')])]), 
        Token('LPAR', '('), 
        Token('RPAR', ')')]), 
    Token('SEMICOLON', ';')])


