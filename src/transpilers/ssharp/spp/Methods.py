from lark.visitors import v_args
from lark.tree import Tree
from lark import Token
from src.semantics.types import * 

from src.utils import AppliedTransformer
from src.transpilers.ssharp.spp.Utils import * 
import copy

gcMarkAndSweep = \
Tree(Token('RULE', 'spplang_stmt_expr'), [
    Tree(Token('RULE', 'spplang_function_call'), [
        Tree(Token('RULE', 'spplang_struct_access'), [
            Tree(Token('RULE', 'spplang_function_call'), [
                Tree(Token('RULE', 'spplang_struct_access'), [
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'gc')]), 
                    Token('DOT', '.'), 
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'mark')])]), 
                Token('LPAR', '('), Token('RPAR', ')')]), 
            Token('DOT', '.'), 
            Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'sweep')])]), 
        Token('LPAR', '('), 
        Token('RPAR', ')')]), 
    Token('SEMICOLON', ';')])


class Methods(AppliedTransformer):

    @v_args(meta=True)
    def ssharplang_method_definition(self, meta, nodes):
        self.applied = True

        plist = [x for c in zip(
            filter(lambda x:isinstance(x,Tree), nodes[1].children[0].children[1:]), 
            filter(lambda x:isinstance(x,Tree), nodes[3].children[1:-1])) for x in [Tree(Token("RULE", "spplang_parameter_definition"), list(c)), Token("COMMA",",")]]
        if len(plist) > 1: del plist[-1]

        for p in plist:
            if isinstance(p,Tree) and p.children[0].data == "ssharplang_tname":
                p.children[0] = Tree(Token("RULE", "spplang_pointer"), [p.children[0], Token("STAR","*")])

        rtype = Tree(Token("RULE", "spplang_pointer"), [nodes[1].children[1].children[1], Token("STAR","*")]) if nodes[1].children[1].children[1].data == "ssharplang_tname" else nodes[1].children[1].children[1]

        res = Tree(Token('RULE', 'spplang_method_definition'), [
            Token('DEF', 'def'), 
            rtype, 
            nodes[2] if nodes[2].children[0].value != "__init__" else Tree(Token("RULE", "spplang_identifier"), [Token("__ANON__", "start")]), 
            Tree(Token('RULE', 'spplang_parameter_seq_def'), [
                Token('LPAR', '('), 
                *plist,
                Token('RPAR', ')')]), 
            Token('DOES', 'does'), 
            nodes[5],
            Token('SEMICOLON',';')
            ], meta)
        return res

    @v_args(meta=True)
    def ssharplang_block(self, meta, nodes):
        return Tree(Token("RULE", "ssharplang_block"), [n for node in nodes for n in (node if isinstance(node,list) else [node])], meta)

    @v_args(meta=True)
    def ssharplang_return(self, meta, nodes):
        return [copy.deepcopy(gcMarkAndSweep),
                Tree(Token("RULE", "ssharplang_return"),nodes, meta)]

    

def methods(parseTree)->Tree:
    parseTree = Methods().transform(parseTree)
    if importMalloc not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(gcImport))
    if importMemcpy not in parseTree.children: parseTree.children.insert(0, copy.deepcopy(gcRefImport))
    return parseTree
