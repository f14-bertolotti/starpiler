
from lark.visitors import Transformer
from lark.tree import Tree
from lark import Token
from src.transpilers import toString
from src.transpilers import addBeforeReturn
from pathlib import Path

from src.transpilers import isSppLang

# slang memcpy, malloc, and free declarations
from lark import Lark
from src.syntax import Language
from src.syntax.slang import functionDefinition, stmtexpr, functionDeclaration
mallocDeclaration = Lark(Language(functionDeclaration).toLark(), keep_all_tokens=True).parse("def int8* malloc(int64);")
memcpyDeclaration = Lark(Language(functionDeclaration).toLark(), keep_all_tokens=True).parse("def int8* memcpy(int8*, int8*, int64);")
freeDeclaration   = Lark(Language(functionDeclaration).toLark(), keep_all_tokens=True).parse("def void free(int8*);")

class UniqueGenerator:
    def __init__(self, program):
        self.program = program
        self.counter = 0
    def __next__(self):
        while f"_{self.counter}_" in self.program: self.counter += 1
        self.counter += 1
        return f"_{self.counter-1}_"


class SppClassesToSStruct(Transformer):

    def __init__(self, *args, **kwargs):
        self.insertMallocDeclaration = False
        self.insertMemcpyDeclaration = False
        self.insertFreeDeclaration   = False
        self.name2class = dict()

    def transform(self, parseTree):
        self.ugen = UniqueGenerator(toString(parseTree))
        self.unique0 = next(self.ugen)
        return super().transform(parseTree)

    def spplang_start(self, nodes):
        toplevels = [sub for node in nodes for sub in (node if isinstance(node,list) else [node])]
        if self.insertMallocDeclaration: toplevels.insert(0, mallocDeclaration);
        if self.insertMemcpyDeclaration: toplevels.insert(0, memcpyDeclaration);
        if self.insertFreeDeclaration  : toplevels.insert(0,   freeDeclaration);
        return Tree(Token("RULE","spplang_start"), toplevels)


    def __default__(self, data, children, meta):
        return Tree(data, [sub for child in children for sub in (child if isinstance(child, list) else [child])], meta)

    #def spplang_import(self, nodes):
    #    raise ValueError("spplang_import should be removed")
    #
    #def slang_import(self, nodes):
    #    self.ugen.program += Path(nodes[1].children[0].value[1:-1]).read_text()
    #    return Tree(Token("RULE", "slang_import"), nodes)

    def spplang_class(self, nodes):
        # check minimal constraints for spplang rules
        # TODO
        
        # check at most one "end" method 
        endMethods = [node for node in nodes[3:-1] if isinstance(node,Tree) and node.data == "spplang_function_definition" and node.children[2].children[0] == "end" ] 
        if len(endMethods) > 1: raise ValueError("more than one \"end\" methods found")

        # check exactly one "start" method
        startMethods = [node for node in nodes[3:-1] if isinstance(node,Tree) and node.data == "spplang_function_definition" and node.children[2].children[0] == "start"]
        if len(startMethods) != 1: 
            raise ValueError("class has 0 or >1 \"start\" methods")
        
        # add end method if not present
        if len(endMethods) == 0:
            endMethods.append(Lark(Language(functionDefinition).toLark(), keep_all_tokens=True).parse(f"def void end({nodes[1].children[0]}* this) does return;;"))
            endMethods[-1].data = "spplang_function_definition"
            nodes.insert(-1, endMethods[-1])

        # adds &free(this as int8*) before each return in the "end" method;
        self.insertFreeDeclaration = True
        freeStmt = Lark(Language(stmtexpr).toLark(), keep_all_tokens=True).parse("&free(this as int8*);")
        endMethods[-1] = addBeforeReturn(freeStmt, endMethods[-1])
             
        # base struct
        baseStruct = Tree(Token("RULE", "slang_struct"), [
            Token("STRUCT", "struct"), 
            Tree(Token("RULE", "slang_tname"), [nodes[1]]), 
            Token("WITH", "with"), 
            Token("SEMICOLON", ";")])

        additionalFunctions = list()
        for node in nodes[3:-1]:
            if isinstance(node, Tree) and node.data == "spplang_field_declaration":
                # add struct declaration
                baseStruct.children.insert(-1, 
                                           Tree(Token('RULE', 'slang_struct_declaration'), [
                                               node.children[1], 
                                               node.children[2], 
                                               Token('SEMICOLON', ';')])
                                           )
            elif isinstance(node, Tree) and node.data == "spplang_field_definition":
                # add struct definition
                baseStruct.children.insert(-1, 
                                           Tree(Token('RULE', 'slang_struct_definition'), [
                                               node.children[1], 
                                               node.children[2], 
                                               Token('EQUAL', '='), 
                                               node.children[4], 
                                               Token('SEMICOLON', ';')])
                                           )
            elif isinstance(node, Tree) and node.data == "spplang_function_definition":
                uniqueName = next(self.ugen)
                # add function definition in struct
                baseFunctionDefinition = Tree(Token('RULE', 'slang_struct_definition'), [
                                             Tree(Token("RULE","slang_pointer"), [
                                                 Tree(Token("RULE","slang_ftype"), [
                                                     Tree(Token("RULE", "slang_ptype"), [
                                                         Token("LPAR","(")]), 
                                                     Tree(Token("RULE","slang_rtype"), [
                                                         Token("__ANON__","->"), 
                                                         Token("RPAR",")")])]),
                                                 Token("STAR","*")]), 
                                             Tree(Token("RULE","slang_identifier"), [Token("__ANON__", f"{node.children[2].children[0]}")]), 
                                             Token('EQUAL', '='), 
                                             Tree(Token("RULE", "slang_reference"), [Token("AMPERSAND", "&"), Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", f"{uniqueName}{node.children[2].children[0]}")])]), 
                                             Token('SEMICOLON', ';')])
                # add parameter types to function definition type
                for param in filter(lambda x: isinstance(x,Tree), node.children[3].children):
                    baseFunctionDefinition.children[0].children[0].children[0].children.append(param.children[0])
                    baseFunctionDefinition.children[0].children[0].children[0].children.append(Token("COMMA",","))
                # remove last comma
                del baseFunctionDefinition.children[0].children[0].children[0].children[-1]
                # add return type to function definition type
                baseFunctionDefinition.children[0].children[0].children[1].children.insert(-1,node.children[1])
                # add function definition to the base struct
                baseStruct.children.insert(-1, baseFunctionDefinition)
                node.children[2].children[0] = Token("__ANON__", f"{uniqueName}{node.children[2].children[0]}")
                additionalFunctions.append(node)
            elif isinstance(node, Token):
                # add token as is (like commas and semicolons)
                baseStruct.children.insert(-1, node)
            else:
                raise ValueError(f"Unexpected node: {node}")

        return [baseStruct, *additionalFunctions]


    #def spplang_new(self, nodes):
    #    self.insertMallocDeclaration = True
    #    self.insertMemcpyDeclaration = True
    #    rest = Tree(Token("RULE", "slang_function_call"), [
    #        Tree(Token("RULE", "slang_struct_access"), [
    #            Tree(Token("RULE", "slang_round_parenthesized"), [
    #                Token("LPAR", "("), 
    #                Tree(Token("RULE", "slang_auto_assignement"), [
    #                    Token("__ANON__", "auto"),
    #                    Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
    #                    Token("EQUAL", "="), 
    #                    Tree(Token('RULE', 'slang_cast'), [
    #                        Tree(Token('RULE', 'slang_function_call'), [
    #                            Tree(Token('RULE', 'slang_reference'), [
    #                                Token('AMPERSAND', '&'), 
    #                                Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', 'memcpy')])]), 
    #                            Token('LPAR', '('), 
    #                            Tree(Token('RULE', 'slang_expression_sequence'), [
    #                                Tree(Token('RULE', 'slang_function_call'), [
    #                                    Tree(Token('RULE', 'slang_reference'), [
    #                                        Token('AMPERSAND', '&'), 
    #                                        Tree(Token('RULE', 'slang_identifier'), [Token('__ANON__', 'malloc')])]), 
    #                                    Token('LPAR', '('), 
    #                                    Tree(Token('RULE', 'slang_expression_sequence'), [
    #                                        Tree(Token('RULE', 'slang_size_of'), [
    #                                            Token('SIZE', 'size'), 
    #                                            Token('OF', 'of'), 
    #                                            Tree(Token('RULE', 'slang_tname'), [
    #                                                nodes[1]])])]), 
    #                                    Token('RPAR', ')')]), 
    #                                Token('COMMA', ','), 
    #                                Tree(Token('RULE', 'slang_cast'), [
    #                                    Tree(Token('RULE', 'slang_struct_value'), [
    #                                        nodes[1],
    #                                        Token('LBRACE', '{'), 
    #                                        Token('RBRACE', '}')]), 
    #                                    Token('AS', 'as'), 
    #                                    Tree(Token('RULE', 'slang_pointer'), [
    #                                        Tree(Token('RULE', 'slang_int8'), [
    #                                            Token('INT8', 'int8')]), 
    #                                        Token('STAR', '*')])]), 
    #                                Token('COMMA', ','), 
    #                                Tree(Token('RULE', 'slang_size_of'), [
    #                                    Token('SIZE', 'size'), 
    #                                    Token('OF', 'of'), 
    #                                    Tree(Token('RULE', 'slang_tname'), [
    #                                        nodes[1]])])]), 
    #                            Token('RPAR', ')')]), 
    #                        Token('AS', 'as'), 
    #                        Tree(Token('RULE', 'slang_pointer'), [
    #                            Tree(Token('RULE', 'slang_tname'), [nodes[1]]), 
    #                            Token('STAR', '*')])])
    #                    ]), 
    #                Token("RPAR", ")")]), 
    #            Token("DOT", "."), 
    #            Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", "start")])]), 
    #        Token("LPAR", "("), 
    #        Tree(Token("RULE", "slang_expression_sequence"), [
    #            Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
    #            *([] if len(nodes) == 4 else [Token("COMMA", ","), *nodes[3].children])]),
    #        Token("RPAR", ")")])
    #    return rest


    #def spplang_function_call(self, nodes):
    #    if nodes[0].data == "spplang_struct_access":
    #        return Tree(Token("RULE", "slang_function_call"), [
    #            Tree(Token("RULE", "slang_struct_access"), [
    #                Tree(Token("RULE", "slang_round_parenthesized"), [
    #                    Token("LPAR", "("), 
    #                    Tree(Token("RULE", "slang_auto_assignement"), [
    #                        Token("AUTO", "auto"), 
    #                        Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
    #                        Token("EQUAL", "="), 
    #                        nodes[0].children[0]]), 
    #                    Token("RPAR", ")")]), 
    #                Token("DOT", "."), 
    #                nodes[0].children[2]]),
    #            Token("LPAR", "("), 
    #            Tree(Token("RULE", "slang_expression_sequence"), [
    #                Tree(Token("RULE", "slang_identifier"), [Token("__ANON__", self.unique0)]), 
    #                *([Token("COMMA",","), *nodes[2].children] if len(nodes) == 4 else [])]),
    #            Token("RPAR", ")")])


        return Tree(Token("RULE","slang_function_call"), nodes)

def sppClassesToSStruct(parseTree):
    if hasattr(parseTree, "path") and "sppClassesToSStruct" in parseTree.path: raise ValueError("sppClassesToSStruct is applicable only once")
    res = SppClassesToSStruct().transform(parseTree)
    return res



