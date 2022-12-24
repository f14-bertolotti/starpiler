from lark.visitors      import v_args
from src.syntax.spplang import methodDefinition
from src.syntax         import Language
from lark.tree          import Tree
from lark               import Token, Lark
from src.utils          import AppliedTransformer
import copy

startMethod = Lark(Language(methodDefinition).toLark(), keep_all_tokens=True).parse(f"def _* start(_* this) does return this;;")
endMethod   = Lark(Language(methodDefinition).toLark(), keep_all_tokens=True).parse(f"def void end(_* this) does return;;")

class Structs(AppliedTransformer):
    
    @v_args(meta=True)
    def slang_struct(self, meta, nodes):
        self.applied = True

        # create basic class with start method
        classTree = Tree(Token('RULE', 'spplang_class'), [
            Token('CLASS', 'class'), 
            Tree(Token("RULE","spplang_identifier"), [Token("__ANON__", nodes[1].children[0].children[0].value)]), 
            Token('WITH', 'with'),  
            Token('SEMICOLON', ';')], meta)

        
        for node in nodes[3:-1]:
            if node.data == "slang_struct_declaration": 
                if node.children[1].children[0] in {"start","end"} : raise ValueError("cannot translate struct \"start\" or \"end\" fields as they have special meaning in s++;")
                # Add field declaration
                classTree.children.insert(-1, 
                                          Tree(Token('RULE', 'spplang_field_declaration'), [
                                              Token('DEF', 'def'), 
                                              node.children[0], 
                                              node.children[1], 
                                              Token('SEMICOLON', ';')], node.meta)
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
                                              Token('SEMICOLON', ';')], node.meta)
                                          )
            else:
                raise ValueError("Unknown node")

        end   = copy.deepcopy(endMethod)
        start = copy.deepcopy(startMethod)
        end  .children[3].children[1].children[0].children[0].children[0].children[0] = Token("__ANON__", nodes[1].children[0].children[0].value)
        start.children[3].children[1].children[0].children[0].children[0].children[0] = Token("__ANON__", nodes[1].children[0].children[0].value)
        start.children[1].children[0].children[0].children[0] = Token("__ANON__", nodes[1].children[0].children[0].value)


        classTree.children.insert(-1, start)
        classTree.children.insert(-1, end)

        return classTree

def structs(parseTree):
    return Structs().transform(parseTree)


