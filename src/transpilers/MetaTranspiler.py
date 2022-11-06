
from src.transpilers.ToString import toString
import rich
class MetaTranspiler:
    def __init__(self, deltas, exitCondition):
        self.exitCondition = exitCondition
        self.deltas        =        deltas

    def search(self, parseTree):
        parseTree.path = []
        #print(f"\n==== START {self.exitCondition.__name__} ====")
        #print(toString(parseTree))
 
        queue   = [parseTree]
        visited = {parseTree}

        while queue:
            #input()
            parseTree = queue.pop(0)
            #print(parseTree.path)
            if self.exitCondition(parseTree): 
                #print("==== DONE ====")
                #print(toString(parseTree))
                return parseTree

            #if parseTree.path == ['sToSppIdentities']:
            #    import rich
            #    rich.#print(parseTree)


            for delta in self.deltas:
                #print(f"\t{delta.__name__} ",end="")
                try: newParseTree = delta(parseTree)
                except:continue ##print();import traceback; traceback.#print_exc(); continue 
                newParseTree.path = parseTree.path + [delta.__name__]

                if newParseTree not in visited:
                    #print("OK",end="")

                    visited.add(newParseTree)
                    queue.append(newParseTree)
                #print()


        raise ValueError("could not transpile")
 

