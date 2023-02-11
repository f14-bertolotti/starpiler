from lark import Tree, Token
from src.utils import AppliedTransformer

class FFI(AppliedTransformer):

    def reset(self):
        self.applied = False
        return self

    def ssharplang_start(self, nodes):

        nodes.insert(0, Tree(Token('RULE', 'spplang_function_declaration'), [Token('DEF', 'def'), Tree(Token('RULE', 'spplang_void'), [Token('VOID', 'void')]), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'free')]), Tree(Token('RULE', 'spplang_parameter_seq_decl'), [Token('LPAR', '('), Tree(Token('RULE', 'spplang_parameter_declaration'), [Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), Token('STAR', '*')])]), Token('RPAR', ')')]), Token('SEMICOLON', ';')]))
        nodes.insert(1, Tree(Token('RULE', 'spplang_global_assignement'), [Token('DEF', 'def'), Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_ftype'), [Tree(Token('RULE', 'spplang_ptype'), [Token('LPAR', '('), Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), Token('STAR', '*')])]), Tree(Token('RULE', 'spplang_rtype'), [Token('__ANON_9', '->'), Tree(Token('RULE', 'spplang_void'), [Token('VOID', 'void')]), Token('RPAR', ')')])]), Token('STAR', '*')]), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', '__free__')]), Token('EQUAL', '='), Tree(Token('RULE', 'spplang_reference'), [Token('AMPERSAND', '&'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', 'free')])]), Token('SEMICOLON', ';')]))
        nodes.insert(2, Tree(Token('RULE', 'spplang_function_declaration'), [Token('DEF', 'def'), Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), Token('STAR', '*')]), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'malloc')]), Tree(Token('RULE', 'spplang_parameter_seq_decl'), [Token('LPAR', '('), Tree(Token('RULE', 'spplang_parameter_declaration'), [Tree(Token('RULE', 'spplang_int64'), [Token('INT64', 'int64')])]), Token('RPAR', ')')]), Token('SEMICOLON', ';')]))
        nodes.insert(3, Tree(Token('RULE', 'spplang_global_assignement'), [Token('DEF', 'def'), Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_ftype'), [Tree(Token('RULE', 'spplang_ptype'), [Token('LPAR', '('), Tree(Token('RULE', 'spplang_int64'), [Token('INT64', 'int64')])]), Tree(Token('RULE', 'spplang_rtype'), [Token('__ANON_9', '->'), Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), Token('STAR', '*')]), Token('RPAR', ')')])]), Token('STAR', '*')]), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', '__malloc__')]), Token('EQUAL', '='), Tree(Token('RULE', 'spplang_reference'), [Token('AMPERSAND', '&'), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', 'malloc')])]), Token('SEMICOLON', ';')]))
        
        return Tree(Token("RULE", "ssharplang_start"), nodes)

                                                                           

    def ssharplang_class_definition(self, nodes):
        
        if nodes[1].children[0].value == "FFI":
            self.applied = True

            return Tree(Token('RULE', 'spplang_class'), [
                    Token('CLASS', 'class'), 
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', nodes[1].children[0].value)]), 
                    Token('WITH', 'with'), 
                    *nodes[3:-1],
                    Token('SEMICOLON', ';')])

ffiTransformer = FFI()
def ffi(parseTree):
    return ffiTransformer.reset().transform(parseTree)



