from src.syntax import Production

import re

def getChangePrefixVisitor(srcPrefix, tgtPrefix):
    def changePrefix(obj):
        if isinstance(obj, Production) and obj.name.startswith(srcPrefix): 
            obj.name = re.sub(f"^{srcPrefix}", tgtPrefix, obj.name)
    return changePrefix


