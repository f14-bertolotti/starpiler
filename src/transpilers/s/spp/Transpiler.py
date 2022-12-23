

from src.transpilers.s.spp import identities
from src.transpilers.s.spp import imports
from src.transpilers.s.spp import structs

def transpile(parseTree):
    for delta in [structs, identities]: 
        try: parseTree = delta(parseTree)
        except Exception as e: 
            #import traceback; 
            #traceback.print_exc(); 
            #print(delta, e);
            #print(("="*20+"\n")*5); 
            continue
    return parseTree


