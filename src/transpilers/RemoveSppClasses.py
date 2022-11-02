
from lark.visitors import Transformer
from lark.tree import Tree
from lark import Token
from src.transpilers import toString
from src.transpilers import addBeforeReturn
from pathlib import Path

class UniqueGenerator:
    def __init__(self, program):
        self.program = program
        self.counter = 0
    def __next__(self):
        while f"_{self.counter}_" in self.program: self.counter += 1
        self.counter += 1
        return f"_{self.counter-1}_"

class RemoveSppClasses(Transformer):

    def transform(self, parseTree):
        self.ugen = UniqueGenerator(toString(parseTree))
        self.unique0 = next(self.ugen)
        return super().transform(parseTree)

    def spplang_start(self, nodes):
        mallocDeclaration = Tree(Token('RULE', 'slang_function_declaration'), [
        Token('DEF', 'def'), 
        Tree(Token('RULE', 'slang_pointer'), [
            Tree(Token('RULE', 'slang_int8'), [
                Token('INT8', 'int8')]), 
            Token('STAR', '*')]), 
        Tree(Token('RULE', 'slang_identifier'), [
            Token('__ANON__', 'malloc')]), 
        Tree(Token('RULE', 'slang_parameter_seq_decl'), [
            Token('LPAR', '('), 
            Tree(Token('RULE', 'slang_parameter_declaration'), [
                Tree(Token('RULE', 'slang_int64'), [
                    Token('INT64', 'int64')])]), 
            Token('RPAR', ')')]), 
        Token('SEMICOLON', ';')])
        memcpyDeclaration = Tree(Token('RULE', 'slang_function_declaration'), [
        Token('DEF', 'def'), 
        Tree(Token('RULE', 'slang_pointer'), [
            Tree(Token('RULE', 'slang_int8'), [
                Token('INT8', 'int8')]), 
            Token('STAR', '*')]), 
        Tree(Token('RULE', 'slang_identifier'), [
            Token('__ANON__', 'memcpy')]), 
        Tree(Token('RULE', 'slang_parameter_seq_decl'), [
            Token('LPAR', '('), 
            Tree(Token('RULE', 'slang_parameter_declaration'), [
                Tree(Token('RULE', 'slang_pointer'), [
                    Tree(Token('RULE', 'slang_int8'), [
                        Token('INT8', 'int8')]), 
                    Token('STAR', '*')])]), 
            Token('COMMA', ','), 
            Tree(Token('RULE', 'slang_parameter_declaration'), [
                Tree(Token('RULE', 'slang_pointer'), [
                    Tree(Token('RULE', 'slang_int8'), [
                        Token('INT8', 'int8')]), 
                    Token('STAR', '*')])]), 
            Token('COMMA', ','), 
            Tree(Token('RULE', 'slang_parameter_declaration'), [
                Tree(Token('RULE', 'slang_int64'), [
                    Token('INT64', 'int64')])]), 
            Token('RPAR', ')')]), 
        Token('SEMICOLON', ';')])
        freeDeclaration = Tree(Token('RULE', 'slang_function_declaration'), [
            Token('DEF', 'def'), 
            Tree(Token('RULE', 'slang_void'), [
                Token('VOID', 'void')]), 
            Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', 'free')]), 
            Tree(Token('RULE', 'slang_parameter_seq_decl'), [
                Token('LPAR', '('), 
                Tree(Token('RULE', 'slang_parameter_declaration'), [
                    Tree(Token('RULE', 'slang_pointer'), [
                        Tree(Token('RULE', 'slang_int8'), [
                            Token('INT8', 'int8')]), Token('STAR', '*')])]), 
                Token('RPAR', ')')]), 
            Token('SEMICOLON', ';')])
        return Tree(Token("RULE","spplang_start"), [freeDeclaration, mallocDeclaration, memcpyDeclaration] + [sub for node in nodes for sub in (node if isinstance(node,list) else [node])])


    def __default__(self, data, children, meta):
        return Tree(data, [sub for child in children for sub in (child if isinstance(child, list) else [child])], meta)

    def spplang_import(self, nodes):
        raise ValueError("spplang_import should be removed")
    
    def slang_import(self, nodes):
        self.ugen.program += Path(nodes[1].children[0].value[1:-1]).read_text()
        return Tree(Token("RULE", "slang_import"), nodes)

    def spplang_class(self, nodes):

        className    = nodes[1]
        classFields  = [node for node in nodes if isinstance(node,Tree) and node.data == "spplang_field_declaration"]
        classMethods = [node for node in nodes if isinstance(node,Tree) and node.data == "spplang_function_definition"]

        # add the "end" method if there is no "end" method
        if not any(method.children[2].children[0].value == "end" for method in classMethods):

            classMethods.append(Tree(Token('RULE', 'slang_function_definition'), [
                Token('DEF', 'def'), 
                Tree(Token('RULE', 'slang_void'), [Token('VOID', 'void')]), 
                Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', 'end')]), 
                Tree(Token('RULE', 'slang_parameter_seq_def'), [Token('LPAR', '('), Token('RPAR', ')')]), 
                Token('DOES', 'does'), 
                Tree(Token('RULE', 'slang_block'), [
                    Tree(Token('RULE', 'slang_return_void'), [
                        Token('RETURN', 'return'), 
                        Token('SEMICOLON', ';')])]), 
                Token('SEMICOLON', ';')]))

        # adds &free(this as int8*) before each return in the "end" method;
        classMethods = [addBeforeReturn(Tree(Token('RULE', 'slang_stmt_expr'), [
            Tree(Token('RULE', 'slang_function_call'), [
                Tree(Token('RULE', 'slang_reference'), [
                    Token('AMPERSAND', '&'), 
                    Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', 'free')])]), 
                Token('LPAR', '('), 
                Tree(Token('RULE', 'slang_expression_sequence'), [
                    Tree(Token('RULE', 'slang_cast'), [
                        Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', 'this')]), 
                        Token('AS', 'as'), 
                        Tree(Token('RULE', 'slang_pointer'), [Tree(Token('RULE', 'slang_int8'), [Token('INT8', 'int8')]), Token('STAR', '*')])])]), 
                Token('RPAR', ')')]), Token('SEMICOLON', ';')]), method) if method.children[2].children[0].value == "end" else method for method in classMethods] 
                
        methodNames  = [method.children[2].children[0] for method in classMethods]
        uniqueNames  = [next(self.ugen) for _ in range(len(classMethods ))]
        returnTypes  = [method.children[1] for method in classMethods]
        paramTypes   = [[node.children[0] for node in method.children[3].children[1:-1:2]] for method in classMethods]
        methodTypes  = [Tree(Token("RULE","slang_pointer"), [Tree(Token("RULE","slang_ftype"),[Tree(Token("RULE", "slang_ptype"), 
                                                               [Token("LPAR","("), 
                                                                *[x for partype in paramstype for x in [partype, Token("COMMA",",")]][:-1]]), 
                                                             Tree(Token("RULE","slang_rtype"), 
                                                               [Token("__ANON__","->"), 
                                                                rettype, 
                                                                Token("RPAR",")")])]),
                                                             Token("STAR","*")]) 
                        for rettype,paramstype in zip(returnTypes, paramTypes)] 

        struct = Tree(Token("RULE", "slang_struct"), [
            Token("STRUCT", "struct"), 
            Tree(Token("RULE", "slang_tname"), [className]), 
            Token("WITH", "with"), 
            *[Tree(Token("RULE", "slang_struct_declaration"), [field.children[1], field.children[2], Token("SEMICOLON",";")]) for field in classFields],
            *[Tree(Token("RULE", "slang_struct_definition"), [
                mtype, 
                Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", mname)]), 
                Token("EQUAL", "="), 
                Tree(Token("RULE", "slang_reference"), [Token("AMPERSAND", "&"), Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", muniq+mname)])]),
                Token("SEMICOLON", ";")]) for mname,mtype,muniq in zip(methodNames, methodTypes, uniqueNames)], 
            Token("SEMICOLON", ";")])

        methodCopies = [Transformer().transform(method) for method in classMethods ]
        for method,unique in zip(methodCopies,uniqueNames): method.children[2].children[0] = Token("__ANON__", unique + method.children[2].children[0].value)
        
        return [struct, *methodCopies]

    def spplang_new(self, nodes):
        rest = Tree(Token("RULE", "slang_function_call"), [
            Tree(Token("RULE", "slang_struct_access"), [
                Tree(Token("RULE", "slang_round_parenthesized"), [
                    Token("LPAR", "("), 
                    Tree(Token("RULE", "slang_auto_assignement"), [
                        Token("__ANON__", "auto"),
                        Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
                        Token("EQUAL", "="), 
                        Tree(Token('RULE', 'slang_cast'), [
                            Tree(Token('RULE', 'slang_function_call'), [
                                Tree(Token('RULE', 'slang_reference'), [
                                    Token('AMPERSAND', '&'), 
                                    Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', 'memcpy')])]), 
                                Token('LPAR', '('), 
                                Tree(Token('RULE', 'slang_expression_sequence'), [
                                    Tree(Token('RULE', 'slang_function_call'), [
                                        Tree(Token('RULE', 'slang_reference'), [
                                            Token('AMPERSAND', '&'), 
                                            Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', 'malloc')])]), 
                                        Token('LPAR', '('), 
                                        Tree(Token('RULE', 'slang_expression_sequence'), [
                                            Tree(Token('RULE', 'slang_size_of'), [
                                                Token('SIZE', 'size'), 
                                                Token('OF', 'of'), 
                                                Tree(Token('RULE', 'slang_tname'), [
                                                    nodes[1]])])]), 
                                        Token('RPAR', ')')]), 
                                    Token('COMMA', ','), 
                                    Tree(Token('RULE', 'slang_cast'), [
                                        Tree(Token('RULE', 'slang_struct_value'), [
                                            nodes[1],
                                            Token('LBRACE', '{'), 
                                            Token('RBRACE', '}')]), 
                                        Token('AS', 'as'), 
                                        Tree(Token('RULE', 'slang_pointer'), [
                                            Tree(Token('RULE', 'slang_int8'), [
                                                Token('INT8', 'int8')]), 
                                            Token('STAR', '*')])]), 
                                    Token('COMMA', ','), 
                                    Tree(Token('RULE', 'slang_size_of'), [
                                        Token('SIZE', 'size'), 
                                        Token('OF', 'of'), 
                                        Tree(Token('RULE', 'slang_tname'), [
                                            nodes[1]])])]), 
                                Token('RPAR', ')')]), 
                            Token('AS', 'as'), 
                            Tree(Token('RULE', 'slang_pointer'), [
                                Tree(Token('RULE', 'slang_tname'), [nodes[1]]), 
                                Token('STAR', '*')])])
                        ]), 
                    Token("RPAR", ")")]), 
                Token("DOT", "."), 
                Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", "start")])]), 
            Token("LPAR", "("), 
            Tree(Token("RULE", "slang_expression_sequence"), [
                Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
                *([] if len(nodes) == 4 else [Token("COMMA", ","), *nodes[3].children])]),
            Token("RPAR", ")")])
        return rest


    def spplang_function_call(self, nodes):
        if nodes[0].data == "spplang_struct_access":
            return Tree(Token("RULE", "slang_function_call"), [
                Tree(Token("RULE", "slang_struct_access"), [
                    Tree(Token("RULE", "slang_round_parenthesized"), [
                        Token("LPAR", "("), 
                        Tree(Token("RULE", "slang_auto_assignement"), [
                            Token("AUTO", "auto"), 
                            Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
                            Token("EQUAL", "="), 
                            nodes[0].children[0]]), 
                        Token("RPAR", ")")]), 
                    Token("DOT", "."), 
                    nodes[0].children[2]]),
                Token("LPAR", "("), 
                Tree(Token("RULE", "slang_expression_sequence"), [
                    Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
                    *([Token("COMMA",","), *nodes[2].children] if len(nodes) == 4 else [])]),
                Token("RPAR", ")")])


        return Tree(Token("RULE","slang_function_call"), nodes)

def removeSppClasses(parseTree):
    res = RemoveSppClasses().transform(parseTree)
    return res


