from lark.visitors import Transformer
from lark import Tree, Token
from src.transpilers.ssharp.spp.Utils import gcPop, importMalloc, importMemcpy
from src.utils.Exceptions import NotAppliedException
import copy

class News(Transformer):
    """ translates news into (auto __ = gc.push(&__memcpy__(&__malloc__(size of TYPE),
                                                            TYPE{} as int8*, 
                                                            size of TYPE),
                                                size of TYPE) as TYPE*)
                                          .start(100);
        returns (translated tree,
                 number of translations)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.news = 0

    def transform(self, *args, **kwargs):
        return super().transform(*args, **kwargs), self.news

    def reset(self):
        self.news = 0
        return self

    def ssharplang_new(self, nodes):
        self.news += 1
        return Tree(Token('RULE', 'spplang_function_call'), [
            Tree(Token('RULE', 'spplang_struct_access'), [
                Tree(Token('RULE', 'spplang_round_parenthesized'), [
                    Token('LPAR', '('), 
                    Tree(Token('RULE', 'spplang_auto_assignement'), [
                        Token('AUTO', 'auto'), 
                        Tree(Token('RULE', 'spplang_identifier'), [
                            Token('__ANON_1', '__')]), 
                        Token('EQUAL', '='), 
                        Tree(Token('RULE', 'spplang_cast'), [
                            Tree(Token('RULE', 'spplang_function_call'), [
                                Tree(Token('RULE', 'spplang_struct_access'), [
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                                    Token('DOT', '.'), 
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'push')])]), 
                                Token('LPAR', '('), 
                                Tree(Token('RULE', 'spplang_expression_sequence'), [
                                    Tree(Token('RULE', 'spplang_function_call'), [
                                        Tree(Token('RULE', 'spplang_reference'), [
                                            Token('AMPERSAND', '&'), 
                                            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__memcpy__')])]), 
                                        Token('LPAR', '('), 
                                        Tree(Token('RULE', 'spplang_expression_sequence'), [
                                            Tree(Token('RULE', 'spplang_function_call'), [
                                                Tree(Token('RULE', 'spplang_reference'), [
                                                    Token('AMPERSAND', '&'), 
                                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', '__malloc__')])]), 
                                                Token('LPAR', '('), 
                                                Tree(Token('RULE', 'spplang_expression_sequence'), [
                                                    Tree(Token('RULE', 'spplang_size_of'), [
                                                        Token('SIZE', 'size'), 
                                                        Token('OF', 'of'), 
                                                        Tree(Token('RULE', 'spplang_tname'), [nodes[1]])])]), 
                                                Token('RPAR', ')')]), 
                                            Token('COMMA', ','), 
                                            Tree(Token('RULE', 'spplang_cast'), [
                                                Tree(Token('RULE', 'spplang_struct_value'), [
                                                    nodes[1], 
                                                    Token('LBRACE', '{'), 
                                                    Token('RBRACE', '}')]), 
                                                Token('AS', 'as'), 
                                                Tree(Token('RULE', 'spplang_pointer'), [
                                                    Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), 
                                                    Token('STAR', '*')])]), 
                                            Token('COMMA', ','), 
                                            Tree(Token('RULE', 'spplang_size_of'), [
                                                Token('SIZE', 'size'), 
                                                Token('OF', 'of'), 
                                                Tree(Token('RULE', 'spplang_tname'), [nodes[1]])])]), 
                                        Token('RPAR', ')')]),
                                Token('COMMA',','),
                                Tree(Token('RULE', 'spplang_size_of'), [
                                    Token('SIZE', 'size'), 
                                    Token('OF', 'of'), 
                                    Tree(Token('RULE', 'spplang_tname'), [nodes[1]])])]), 
                                Token('RPAR', ')')]), 
                            Token('AS', 'as'), 
                            Tree(Token('RULE', 'spplang_pointer'), [
                                Tree(Token('RULE', 'spplang_tname'), [
                                    nodes[1]]), 
                                Token('STAR', '*')])])]), 
                    Token('RPAR', ')')]), 
                Token('DOT', '.'), 
                Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'start')])]), 
            Token('LPAR', '('), 
            nodes[3], 
            Token('RPAR', ')')])

class BlockTransformer(Transformer):
    """
        translates news.
        for each new translated adds a gc.pop() at the of the block
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applied = False
        self.newsTransformer = News()

    def reset(self):
        self.applied = False
        self.newsTransformer.reset()
        return self

    def transform(self, *args, **kwargs):
        self.reset()
        result = super().transform(*args, **kwargs)
        if not (self.applied > 0): raise NotAppliedException("could not apply")
        return result
    
    def ssharplang_block(self, nodes):
        tree = Tree(Token("RULE","ssharplang_block"), nodes)
        tree, news = self.newsTransformer.reset().transform(tree) # translates ssharplang_new
        self.applied = self.applied or (news > 0) # if a translation is performed this tranformer has been applied

        # adds gc.pop() before the last statement if the last statement is a ssharplang_return
        # otherwise adds gc.pop() as the last statements
        pops = [copy.deepcopy(gcPop) for _ in range(news)]
        tree.children = tree.children[:-1] + pops + [tree.children[-1]] if tree.children[-1].data == "ssharplang_return" else tree.children + pops
        return tree



blockTransformer = BlockTransformer()
def news(parseTree):
    """
    explores block rules.
    transform each ssharplang_new into spplnag equivalent (auto __ = gc.push(&__memcpy__(&__malloc__(size of TYPE),
                                                                                         TYPE{} as int8*, 
                                                                                         size of TYPE),
                                                                             size of TYPE) as TYPE*)
                                                                       .start(100);
    for each push adds a gc.pop() add the end of the respective block
    if not already presents adds 
        1) from "src/testing/spplang/programs/gc/GC.spp" import malloc as __malloc__ ;
        2) from "src/testing/spplang/programs/gc/GC.spp" import memcpy as __memcpy__ ;
    """
    parseTree = blockTransformer.reset().transform(parseTree)
    if importMalloc not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMalloc))
    if importMemcpy not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(importMemcpy))
    return parseTree



