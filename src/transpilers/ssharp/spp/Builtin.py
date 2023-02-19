from lark.visitors import Transformer
from lark import Tree, Token
import lark

from src.utils import NotAppliedException
from src.transpilers.ssharp.spp.Utils import gcMarkAndSweep
import copy

class Builtin(Transformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hasPrint = False
        self.applied = False

    def reset(self):
        self.hasPrint = False
        self.applied = False
        return self

    def transform(self, tree):
        try:
            tree = super().transform(tree)
            if not self.applied: raise NotAppliedException()
            return tree
        except lark.exceptions.VisitError: raise NotAppliedException()

    def ssharplang_start(self, nodes):

        if not any([node.data == "ssharplang_class_definition" for node in nodes if isinstance(node,Tree)]): raise ValueError("no ssharplang_class_definition found")

        for i,node in enumerate(nodes): 
            if isinstance(node, Tree) and node.data == "ssharplang_class_definition":
                break

        if self.hasPrint and self.applied: nodes.insert(i,Tree(Token('RULE', 'spplang_function_declaration'), [Token('DEF', 'def'), Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), Token('STAR', '*')]), Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'printf')]), Tree(Token('RULE', 'spplang_parameter_seq_decl'), [Token('LPAR', '('), Tree(Token('RULE', 'spplang_parameter_declaration'), [Tree(Token('RULE', 'spplang_pointer'), [Tree(Token('RULE', 'spplang_int8'), [Token('INT8', 'int8')]), Token('STAR', '*')])]), Token('COMMA', ','), Tree(Token('RULE', 'spplang_parameter_declaration'), [Tree(Token('RULE', 'spplang_vararg_parameter'), [Token('__ANON__', '...')])]), Token('RPAR', ')')]), Token('SEMICOLON', ';')]))
        return Tree(Token("RULE", "ssharplang_start"), nodes)

    def ssharplang_function_call(self, nodes):

        if not all([node.data.startswith("ssharplang_") for node in nodes if isinstance(node, Tree)]): raise ValueError("translated subtrees")

        self.applied = True
        if nodes[0].data == "ssharplang_identifier" and nodes[0].children[0].value == "print":
            self.hasPrint = True
            return \
            Tree(Token('RULE', 'spplang_function_call'), [
                Tree(Token('RULE', 'spplang_reference'), [
                    Token('AMPERSAND', '&'), 
                    Tree(Token('RULE', 'spplang_identifier'), [Token('__ANON__', 'printf')])]), 
                Token('LPAR', '('), 
                nodes[2],
                Token('RPAR', ')')])

        elif nodes[0].data == "ssharplang_identifier" and nodes[0].children[0].value == "gccollect":
            self.hasCollect = True
            return copy.deepcopy(gcMarkAndSweep)


        return Tree(Token("RULE", "spplang_function_call"), nodes)


builtinTransformer= Builtin()

def builtin(parseTree):
    return builtinTransformer.reset().transform(parseTree)
