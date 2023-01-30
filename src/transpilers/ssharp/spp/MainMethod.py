from lark.visitors import Visitor
from lark import Tree, Token
from src.utils import AppliedTransformer
from src.transpilers.ssharp.spp.Utils import *

import copy

def getTempResultAssigement(value):
    return \
    Tree(Token('RULE', 'ssharplang_stmt_expr'), [
        Tree(Token('RULE', 'ssharplang_declaration_assignment'), [
            Tree(Token('RULE', 'ssharplang_int64'), [Token('INT64', 'int64')]), 
            Tree(Token('RULE', 'ssharplang_identifier'), [Token('__ANON__', '__result__')]), 
            Token('EQUAL', '='), 
            value]), 
        Token('SEMICOLON', ';')])

def getReturnResultTree():
    return \
    Tree(Token('RULE', 'spplang_return'), [
        Token('RETURN', 'return'), 
        Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__result__')]), 
        Token('SEMICOLON', ';')])


class EndGC(Visitor):
    def ssharplang_block(self, tree):
        tree.children = [c for child in tree.children for c in ([getTempResultAssigement(child.children[1]), copy.deepcopy(gcEnd), getReturnResultTree()] if isinstance(child, Tree) and child.data == "ssharplang_return" else [child])]

class MainMethod(AppliedTransformer):

    def __init__(self, *args, **kwargs):
        self.mainMethod = None
        self.endGCVisitor = EndGC()
        super().__init__(*args, **kwargs)

    def reset(self):
        self.applied, self.mainMethod = False, None
        return self

    def ssharplang_start(self, nodes): 
        if self.mainMethod == None: raise ValueError("no required __main__ method found.") 
        nodes.append(self.mainMethod)
        return Tree(Token('RULE', 'ssharplang_start'), nodes)

    def ssharplang_method_definition(self, nodes):

        if nodes[2].children[0] == "__main__" and \
           nodes[1].data == "ssharplang_ftype" and \
           nodes[1].children[0].data == "ssharplang_ptype" and \
           nodes[1].children[1].data == "ssharplang_rtype" and \
           nodes[1].children[1].children[1].data == "ssharplang_int64": 
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
        return Tree(Token("RULE", "ssharplang_class_definition"), [node for node in nodes if node != None])

mainMethodTransformer = MainMethod()
def mainMethod(parseTree):
    parseTree = mainMethodTransformer.reset().transform(parseTree)
    if importGC not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importGC))
    if importgc not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importgc))
    return parseTree

