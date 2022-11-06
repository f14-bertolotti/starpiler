from lark import Lark, Token
from lark.tree import Tree
from lark.visitors import Transformer
from src.syntax.spplang import methodDefinition
from src.syntax import Language

class SStructToSppClass(Transformer):

    def slang_struct(self, nodes):

        # create basic class with start method
        classTree = Tree(Token('RULE', 'spplang_class'), [
            Token('CLASS', 'class'), 
            nodes[1].children[0], 
            Token('WITH', 'with'),  
            Token('SEMICOLON', ';')])

        
        for node in nodes[3:-1]:
            if node.data == "slang_struct_declaration": 
                if node.children[1].children[0] in {"start","end"} : raise ValueError("cannot translate struct \"start\" or \"end\" fields as they have special meaning in s++;")
                # Add field declaration
                classTree.children.insert(-1, 
                                          Tree(Token('RULE', 'spplang_field_declaration'), [
                                              Token('DEF', 'def'), 
                                              node.children[0], 
                                              node.children[1], 
                                              Token('SEMICOLON', ';')])
                                          )
                
            elif node.data == "slang_struct_definition": 
                if node.children[1].children[0] in {"start","end"} : raise ValueError("cannot translate struct \"start\" or \"end\" fields as they have special meaning in s++;")
                # Add field definition
                classTree.children.insert(-1, 
                                          Tree(Token('RULE', 'spplang_field_definition'), [
                                              Token('DEF', 'def'), 
                                              node.children[0], 
                                              node.children[1],
                                              Token("EQUAL", "="),
                                              node.children[3],
                                              Token('SEMICOLON', ';')]))
            else:
                raise ValueError("Unknown node")

        classTree.children.insert(-1, Lark(Language(methodDefinition).toLark(), keep_all_tokens=True).parse(f"def {nodes[1].children[0].children[0].value}* start({nodes[1].children[0].children[0].value}* this) does return this;;"))
        classTree.children.insert(-1, Lark(Language(methodDefinition).toLark(), keep_all_tokens=True).parse(f"def void end({nodes[1].children[0].children[0].value}* this) does &free(this as int8*);return;;"))

        return classTree

def sStructToSppClass(parseTree):
    return SStructToSppClass().transform(parseTree)


