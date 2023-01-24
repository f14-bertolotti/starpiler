from lark.visitors import v_args, Visitor
from src.utils import AppliedTransformer
from src.utils import NotAppliedException
from src.utils import SmallMeta


from lark import Tree, Token
import copy

from src.transpilers.ssharp.spp.News import mainNews
from src.transpilers.ssharp.spp.NewOfs import mainNewofs
from src.transpilers.ssharp.spp.Utils import *



sppMainMethod = \
Tree(Token('RULE', 'spplang_function_definition'), [
    Token('DEF', 'def'), 
    Tree(Token('RULE', 'spplang_int64'), [Token('INT64', 'int64')]), 
    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'start')]), 
    Tree(Token('RULE', 'spplang_parameter_seq_def'), [Token('LPAR', '('), Token('RPAR', ')')]), 
    Token('DOES', 'does'), 
    Tree(Token('RULE', 'spplang_block'), [
        Tree(Token('RULE', 'spplang_stmt_expr'), [
            Tree(Token('RULE', 'spplang_assignement'), [
                Tree(Token('RULE', 'spplang_reference'), [
                    Token('AMPERSAND', '&'), 
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')])]), 
                Token('EQUAL', '='), 
                Tree(Token('RULE', 'spplang_new'), [
                    Token('NEW', 'new'), 
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'GC')]), 
                    Token('LPAR', '('), 
                    Token('RPAR', ')')])]), 
            Token('SEMICOLON', ';')]),]), 
    Token('SEMICOLON', ';')])

gcEnd = \
Tree(Token('RULE', 'spplang_stmt_expr'), [
    Tree(Token('RULE', 'spplang_function_call'), [
        Tree(Token('RULE', 'spplang_struct_access'), [
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
            Token('DOT', '.'), 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'end')])]), 
        Token('LPAR', '('), 
        Token('RPAR', ')')]), 
    Token('SEMICOLON', ';')])



def getTempResultAssigement(value):
    return \
    Tree(Token('RULE', 'spplang_stmt_expr'), [
        Tree(Token('RULE', 'spplang_declaration_assignment'), [
            Tree(Token('RULE', 'spplang_int64'), [Token('INT64', 'int64')]), 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON_1', '__result__')]), 
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
    def spplang_block(self, tree):
        self.ssharplang_block(tree)

class MainMethod(AppliedTransformer):

    def __init__(self, *args, **kwargs):
        self.mainMethod = None
        super().__init__(*args, **kwargs)

    def __default(self, data, children, meta):
        if not data.startswith("ssharplang_"): raise ValueError(f"Only ssharplang nodes allowed. Found {data}")
        return super().__default(data, children, meta)

    @v_args(meta=True)
    def ssharplang_start(self, meta, nodes): 
        if self.mainMethod == None: raise ValueError("no required __main__ method found.") 
        return Tree(Token('RULE', 'ssharplang_start'), nodes + [self.mainMethod], meta)

    @v_args(meta=True)
    def ssharplang_method_definition(self, meta, nodes):

        if nodes[2].children[0] == "__main__" and \
           nodes[1].data == "ssharplang_ftype" and \
           nodes[1].children[0].data == "ssharplang_ptype" and \
           nodes[1].children[1].data == "ssharplang_rtype" and \
           nodes[1].children[1].children[1].data == "ssharplang_int64": 

            self.applied=True
            self.mainMethod = copy.deepcopy(sppMainMethod)
            self.mainMethod.children[5].children += nodes[5].children
            try: self.mainMethod = mainNews(self.mainMethod)
            except NotAppliedException: pass
            try: self.mainMethod = mainNewofs(self.mainMethod)
            except NotAppliedException: pass
            self.mainMethod = EndGC().visit(self.mainMethod)

            return None 

        else:
            return Tree(Token("RULE", "ssharplang_method_definition"), nodes, meta)

    @v_args(meta=True)
    def ssharplang_class_definition(self, meta, nodes):
        return Tree(Token("RULE", "ssharplang_class_definition"), [node for node in nodes if node != None], meta)


def mainMethod(parseTree):
    parseTree = MainMethod().transform(parseTree)
    parseTree.children.insert(0, copy.deepcopy(importMemcpy))
    parseTree.children.insert(0, copy.deepcopy(importMalloc))
    parseTree.children.insert(0, copy.deepcopy(gcRefImport))
    parseTree.children.insert(0, copy.deepcopy(gcImport))
    return parseTree
