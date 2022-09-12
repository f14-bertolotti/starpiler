from lark import Token

def addition(self, tree):
    l,r = tree[0].children[0], tree[1].children[0]
    return f"{l}+{r}" 

def subtraction(self, tree):
    l,r = tree[0].children[0], tree[1].children[0]
    return f"{l}-{r}"

def division(self, tree):
    l,r = tree[0].children[0], tree[1].children[0]
    return f"{l}/{r}"

def multiplication(self, tree):
    l,r = tree[0].children[0], tree[1].children[0]
    return f"{l}*{r}"

def equality(self, tree):
    l,r = tree[0].children[0], tree[1].children[0]
    return f"{l}=={r}"

def inequality(self, tree):
    l,r = tree[0].children[0], tree[1].children[0]
    return f"{l}!={r}"


