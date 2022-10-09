from src.syntax import Language   as L
from src.syntax import Production as P
from src.syntax import Terminal   as T
from src.syntax import Rule       as R


import re

def getChangePrefixVisitor(srcPrefix, tgtPrefix):
    def changePrefix(obj):
        if isinstance(obj, P) and obj.name.startswith(srcPrefix): 
            obj.name = re.sub(f"^{srcPrefix}", tgtPrefix, obj.name)
        return obj
    return changePrefix, set()


def getClonerVisitor(TopObj):
    clones2cloned = dict()
    cloned2clones = dict()
    def cloner(obj):
        
        if isinstance(obj, T): cloned2clones[obj] = T(obj.value[:], obj.regex, obj.mod[:])
        if isinstance(obj, R): cloned2clones[obj] = R(mod=obj.mod[:])
        if isinstance(obj, P): cloned2clones[obj] = P(obj.name[:], rules=[], mod=obj.mod[:])
        if isinstance(obj, L): cloned2clones[obj] = L(obj.production[0])
        clones2cloned[cloned2clones[obj]] = obj

        if obj is TopObj:
            for clones,cloned in clones2cloned.items():
                for child in cloned: 
                    clones.append(cloned2clones[child])
            return cloned2clones[obj]

    return cloner, set()


def getFindAndReplaceVisitor(src, tgt):
    def replacer(obj):

        for i,_ in filter(lambda x: isinstance(x[1], P) and x[1].name == src, enumerate(obj)): 
            obj[i] = tgt

        return obj
    return replacer, set()
        
