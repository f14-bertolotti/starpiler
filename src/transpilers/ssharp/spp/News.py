from lark.visitors import Transformer
from lark import Tree, Token
from src.transpilers.ssharp.spp.Utils import importgc
from src.utils import NotAppliedException
from src.utils import AppliedTransformer

def get_new_assignement(name, typ, params):
    return \
    Tree(Token('RULE', 'spplang_stmt_expr'), [
        Tree(Token('RULE', 'spplang_auto_assignement'), [
            Token('AUTO', 'auto'), 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', name)]), 
            Token('EQUAL', '='), 
            Tree(Token('RULE', 'spplang_function_call'), [
                Tree(Token('RULE', 'spplang_struct_access'), [
                    Tree(Token('RULE', 'spplang_round_parenthesized'), [
                        Token('LPAR', '('), Tree(Token('RULE', 'spplang_cast'), [
                            Tree(Token('RULE', 'spplang_function_call'), [
                                Tree(Token('RULE', 'spplang_struct_access'), [
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                                    Token('DOT', '.'), 
                                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gcmemcpy')])]), 
                                Token('LPAR', '('), 
                                Tree(Token('RULE', 'spplang_expression_sequence'), [
                                    Tree(Token('RULE', 'spplang_size_of'), [
                                        Token('SIZE', 'size'), 
                                        Token('OF', 'of'), 
                                        Tree(Token('RULE', 'spplang_tname'), [typ])]), 
                                    Token('COMMA', ','), 
                                    Tree(Token('RULE', 'spplang_cast'), [
                                        Tree(Token('RULE', 'spplang_struct_value'), [
                                            typ, 
                                            Token('LBRACE', '{'), 
                                            Token('RBRACE', '}')]), 
                                        Token('AS', 'as'), 
                                        Tree(Token('RULE', 'spplang_pointer'), [
                                            Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), 
                                            Token('STAR', '*')])])]), 
                                Token('RPAR', ')')]), 
                            Token('AS', 'as'), 
                            Tree(Token('RULE', 'spplang_pointer'), [
                                Tree(Token('RULE', 'spplang_tname'), [typ]), 
                                Token('STAR', '*')])]), 
                        Token('RPAR', ')')]), 
                    Token('DOT', '.'), 
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'start')])]), 
                Token('LPAR', '('), 
                *params,
                Token('RPAR', ')')])]), 
        Token('SEMICOLON', ';')])


class News(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assignements = list()

    def transform(self, *args, **kwargs):
        tree = super().transform(*args, **kwargs)
        return tree, self.assignements

    def reset(self):
        self.assignements.clear()
        return self

    def ssharplang_new(self, nodes):
        name = f"__{len(self.assignements)}_"
        self.assignements.append(get_new_assignement(name, nodes[1], [nodes[3]] if len(nodes) == 5 else []))
        return Tree(Token("RULE","spplang_identifier"), [Token("__ANON__", name)]) 
        

class BlockTransformer(Transformer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.news = News()
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
            node, ass = self.news.reset().transform(node)
            future_pops += len(ass) 
            newnodes = newnodes + ass + [node]

        if future_pops > 0: self.applied = True
    
        return Tree(Token("RULE", "ssharplang_pop_block"), newnodes + [future_pops])

    
blockTransformer = BlockTransformer()
def news(parseTree):
    parseTree = blockTransformer.reset().transform(parseTree)
    return parseTree



