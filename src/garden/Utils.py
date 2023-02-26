import pickle

def dump(obj, path):
    with open(path, 'wb') as file:
        pickle.dump(obj, file)

class Node:
    def __init__(self, tree, rsdd, issol=False, isroot=False, genfrom=None):
        self.tree, self.rsdd = tree, rsdd
        self.issol, self.isroot = issol, isroot
        self.genfrom = genfrom

    def __hash__(self):
        return hash(self.tree)

    def __eq__(self, other):
        return self.tree == other.tree

    def __neq__(self, other):
        return self.tree != other.tree


