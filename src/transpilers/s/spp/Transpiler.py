

from src.transpilers.s.spp import identities
from src.transpilers.s.spp import imports
from src.transpilers.s.spp import structs
from src.transpilers.s.spp import globalAssignements

from src.utils import NotAppliedException


deltas = [structs, globalAssignements, imports, identities]

def transpile(parseTree):
    for delta in deltas: 
        try: parseTree = delta(parseTree)
        except NotAppliedException: continue
    return parseTree

