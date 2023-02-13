from lark.visitors import Transformer, Visitor
from lark import Tree, Token
from src.utils import NotAppliedException
from src.transpilers.ssharp.spp.Utils import *

import copy

def getTempResultAssigement(value):
    return \
        Tree(Token('RULE', 'ssharplang_declaration_assignment'), [
            Tree(Token('RULE', 'ssharplang_int64'), [Token('INT64', 'int64')]), 
            Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', '__result__')]), 
            Token('EQUAL', '='), 
            value,
            Token('SEMICOLON', ';')])

def getReturnResultTree():
    return \
    Tree(Token('RULE', 'ssharplang_return'), [
        Token('RETURN', 'return'), 
        Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', '__result__')]), 
        Token('SEMICOLON', ';')])


class EndGC(Visitor):
    def ssharplang_block(self, tree):

        if isinstance(tree.children[-1], Tree) and tree.children[-1].data == "ssharplang_return":
            if gcPop in tree.children: 
                tree.children.insert(tree.children.index(gcPop),getTempResultAssigement(tree.children[-1].children[1]))
            else:
                tree.children.insert(-1, getTempResultAssigement(tree.children[-1].children[1]))
            tree.children.insert(-1, copy.deepcopy(gcEnd))
            tree.children[-1] = getReturnResultTree()

        
class MainMethod(Transformer):

    def __init__(self, *args, **kwargs):
        self.mainMethod = None
        self.endGCVisitor = EndGC()
        self.removedNode = False
        self.mainMethodInserted = False
        self.applied = False
        super().__init__(*args, **kwargs)

    def transform(self, *args, **kwargs):
        result = super().transform(*args, **kwargs)
        if self.applied == False or self.mainMethodInserted == False or self.removedNone == False: raise NotAppliedException("MainMethod not applied")
        return result

    def reset(self):
        self.applied, self.mainMethod = False, None
        self.removedNone = False
        self.mainMethodInserted = False
        return self

    def ssharplang_start(self, nodes): 
        if self.mainMethod != None:
            self.mainMethodInserted = True
            nodes.append(self.mainMethod)
        return Tree(Token('RULE', 'ssharplang_start'), nodes)

    def ssharplang_method_definition(self, nodes):

        if is_main_method(nodes): 

            # if it is a main method
            self.applied=True
            self.mainMethod = copy.deepcopy(sppMainMethod)
            self.mainMethod.children[5].children += nodes[5].children
            self.mainMethod = self.endGCVisitor.visit(self.mainMethod)
            return None 

        else:
            # if it is a normal method
            return Tree(Token("RULE", "ssharplang_method_definition"), nodes)

    def ssharplang_class_definition(self, nodes):
        # remove the None child from the class which may be present if there was a main method in the class
        self.removedNone = True
        return Tree(Token("RULE", "ssharplang_class_definition"), [node for node in nodes if node != None])

mainMethodTransformer = MainMethod()
def mainMethod(parseTree):
    parseTree = mainMethodTransformer.reset().transform(parseTree)
    if importGC not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importGC))
    if importgc not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importgc))
    return parseTree

