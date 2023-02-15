
from src.transpilers.ssharp.spp import classes
from src.transpilers.ssharp.spp import assignements
from src.transpilers.ssharp.spp import methods
from src.transpilers.ssharp.spp import functionCalls, ifs, builtin, indexes, newof_natives, futurepops_ssharp, fors, whiles, arrays, classAccesses, news, newofs
from src.transpilers.ssharp.spp import identities
from src.transpilers.ssharp.spp import mainMethod
from src.transpilers.ssharp.spp import imports
from src.transpilers.ssharp.spp import fields

from src.utils import NotAppliedException

def transpile(parseTree):
    for delta in [mainMethod, news, futurepops_ssharp, newof_natives, futurepops_ssharp, newofs, futurepops_ssharp, builtin, functionCalls, ifs, fors, whiles, classes, fields, assignements, indexes, methods, arrays, classAccesses, imports, identities]: 
        try: parseTree = delta(parseTree)
        except NotAppliedException as e: pass 

    return parseTree

deltas = [[mainMethod, methods], 
          [news, futurepops_ssharp, newof_natives, futurepops_ssharp, newofs, futurepops_ssharp], 
          [builtin, functionCalls], 
          [ifs, fors, whiles, assignements],
          [classes, fields, indexes, arrays, classAccesses], imports, identities]
