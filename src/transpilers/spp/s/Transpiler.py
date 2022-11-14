
from src.transpilers.spp.s import classes
from src.transpilers.spp.s import globalAssignements
from src.transpilers.spp.s import identities
from src.transpilers.spp.s import imports
from src.transpilers.spp.s import news
from src.transpilers.spp.s import classAccesses

from src.transpilers.spp import types
from src.transpilers.spp import addEndMethods

from src.utils import SPrettyPrinter

def transpile(parseTree):
    for delta in [addEndMethods, types, classes, news, classAccesses, imports, globalAssignements, identities]: 
        try: parseTree = delta(parseTree)
        except Exception as e: continue #import traceback; traceback.print_exc(); print(delta, e);print(("="*20+"\n")*5); continue
    return parseTree


deltas = [types, globalAssignements, imports, news, addEndMethods, classAccesses, classes, identities]
