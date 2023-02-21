
from src.transpilers.ssharp.spp import classes
from src.transpilers.ssharp.spp import assignements
from src.transpilers.ssharp.spp import methods
from src.transpilers.ssharp.spp import ifs, builtin, indexes, newof_natives, futurepops_ssharp, fors, whiles, arrays, classAccesses, news, newofs
from src.transpilers.ssharp.spp import identities
from src.transpilers.ssharp.spp import mainMethod
from src.transpilers.ssharp.spp import imports
from src.transpilers.ssharp.spp import fields

from src.utils import NotAppliedException
from src.utils import merge_delta


deltas = [merge_delta([mainMethod, methods]), 
          merge_delta([news, futurepops_ssharp]), 
          merge_delta([newof_natives, futurepops_ssharp]), 
          merge_delta([newofs, futurepops_ssharp]), 
          builtin, 
          ifs, fors, whiles, assignements,
          classes, fields, indexes, arrays, classAccesses, imports, identities]

def transpile(parseTree):
    for delta in deltas: 
        try: parseTree = delta(parseTree)
        except NotAppliedException as e: pass 

    return parseTree


