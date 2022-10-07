from src.syntax import Language   as L
from src.syntax import Production as P
from src.syntax import Terminal   as T
from src.syntax import Rule       as R


import re

def getChangePrefixVisitor(srcPrefix, tgtPrefix):
    def changePrefix(obj):
        if isinstance(obj, P) and obj.name.startswith(srcPrefix): 
            obj.name = re.sub(f"^{srcPrefix}", tgtPrefix, obj.name)
    return changePrefix, set()

def getClonerVisitor():
    clones2cloned = dict()
    cloned2clones = dict()
    def cloner(obj):
        
        if isinstance(obj, L):
            for clones,cloned in clones2cloned.items():
                for child in cloned: 
                    clones.append(cloned2clones[child])
            return L(cloned2clones[obj.production])

        else: 
            if isinstance(obj, T): cloned2clones[obj] = T(obj.value[:], obj.regex, obj.mod[:])
            if isinstance(obj, R): cloned2clones[obj] = R(mod=obj.mod[:])
            if isinstance(obj, P): cloned2clones[obj] = P(obj.name[:], rules=[], mod=obj.mod[:])
            clones2cloned[cloned2clones[obj]] = obj
            return None

    return cloner, set()
        
