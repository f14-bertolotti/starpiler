from lark.visitors import Transformer
from lark import Tree, Token
from src.transpilers.ssharp.spp.Utils import *
from src.utils import NotAppliedException
import copy

class NewOfNatives(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pops = 0

    def reset(self):
        self.pops = 0
        return self

    def transform(self, *args, **kwargs):
        return super().transform(*args, **kwargs), self.pops

    def ssharplang_new_of_native(self, nodes):
        self.pops += 1
        return \
        Tree(Token('RULE', 'spplang_cast'), [
            Tree(Token('RULE', 'spplang_function_call'), [
                Tree(Token('RULE', 'spplang_struct_access'), [
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                    Token('DOT', '.'), 
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gcmalloc')])]), 
                Token('LPAR', '('), Tree(Token('RULE', 'spplang_expression_sequence'), [
                    Tree(Token('RULE', 'spplang_multiplication'), [
                        nodes[1], 
                        Token('STAR', '*'), 
                        Tree(Token('RULE', 'spplang_size_of'), [
                            Token('SIZE', 'size'), 
                            Token('OF', 'of'), 
                            nodes[3]])])]), 
                Token('RPAR', ')')]), 
            Token('AS', 'as'), 
            Tree(Token('RULE', 'spplang_pointer'), [
                nodes[3], 
                Token('STAR', '*')])])


class BlockTransformer(Transformer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.newOfs = NewOfNatives()
        self.applied = False

    def reset(self):
        self.applied = False
        return self

    def transform(self, *args, **kwargs):
        result = super().transform(*args, **kwargs)
        if not self.applied: raise NotAppliedException("BlockTransformer not applied");
        return result

    def ssharplang_start(self, nodes):
        if importgc not in nodes: nodes.insert(0, importgc)
        return Tree(Token("RULE","ssharplang_start"), nodes)

    def ssharplang_block(self, nodes):
        newnodes = list()
        future_pops = 0
        for node in nodes:
            node, pops = self.newOfs.reset().transform(node)
            future_pops += pops
            newnodes.append(node)

        if future_pops > 0: self.applied = True
    
        return Tree(Token("RULE", "ssharplang_pop_block"), newnodes + [future_pops])

    
blockTransformer = BlockTransformer()
def newof_natives(parseTree):
    return blockTransformer.reset().transform(parseTree)


