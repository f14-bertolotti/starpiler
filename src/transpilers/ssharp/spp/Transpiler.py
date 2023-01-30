
from src.transpilers.ssharp.spp import classes
from src.transpilers.ssharp.spp import assignements
from src.transpilers.ssharp.spp import methods
from src.transpilers.ssharp.spp import indexes, fors, whiles, arrays, classAccesses, news, newofs
from src.transpilers.ssharp.spp import identities
from src.transpilers.ssharp.spp import mainMethod
from src.transpilers.ssharp.spp import imports
from src.transpilers.ssharp.spp import fields

from src.utils import NotAppliedException

def transpile(parseTree):
    for delta in [news, newofs, indexes, fors, fors, whiles, mainMethod, classes, fields, assignements, methods, arrays, imports, identities]: 
        try: parseTree = delta(parseTree)
        except NotAppliedException as e: pass 

    return parseTree


deltas = [news, newofs, indexes, whiles, mainMethod, classes, fields, assignements, methods, arrays, imports, identities]
