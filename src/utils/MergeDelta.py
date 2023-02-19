from src.utils import NotAppliedException

def merge_delta(deltas):

    def delta(tree):
        applied = False
        for delta in deltas:
            try:
                newtree = delta(tree)
                tree = newtree
                applied = True
            except NotAppliedException as e: pass

        if not applied: raise NotAppliedException
        return tree

    delta.__name__ = ":".join([delta.__name__ for delta in deltas])

    return delta


