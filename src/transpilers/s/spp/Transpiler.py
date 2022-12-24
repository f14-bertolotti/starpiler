

from src.transpilers.s.spp import identities
from src.transpilers.s.spp import imports
from src.transpilers.s.spp import structs
from src.transpilers.s.spp import globalAssignements

from src.utils import NotAppliedException


deltas = [structs, globalAssignements, imports, identities]

def transpile(parseTree):
    for delta in deltas: 
        try: parseTree = delta(parseTree)
        except NotAppliedException: 
            #import traceback; 
            #traceback.print_exc(); 
            #print(delta, e);
            #print(("="*20+"\n")*5); 
            continue
    return parseTree

