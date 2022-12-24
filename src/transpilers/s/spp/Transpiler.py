

from src.transpilers.s.spp import identities
from src.transpilers.s.spp import imports
from src.transpilers.s.spp import structs
from src.transpilers.s.spp import globalAssignements


deltas = [structs, globalAssignements, imports, identities]

def transpile(parseTree):
    for delta in deltas: 
        try: parseTree = delta(parseTree)
        except ValueError as e: 
            #import traceback; 
            #traceback.print_exc(); 
            #print(delta, e);
            #print(("="*20+"\n")*5); 
            continue
    return parseTree

