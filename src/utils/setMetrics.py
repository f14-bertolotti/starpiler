def set_difference_distance(A, B): 
    return len(A.union(B)) - len(A.intersection(B))

def relative_set_difference_distance(S, A, B):
    if   not A.issubset(S) and not B.issubset(S): return set_difference_distance(A,B)
    elif not A.issubset(S) and     B.issubset(S): return set_difference_distance(A,S)
    elif     A.issubset(S) and not B.issubset(S): return set_difference_distance(S,B)
    elif     A.issubset(S) and     B.issubset(S) and A == B: return 0
    elif     A.issubset(S) and     B.issubset(S) and A != B: return 0.5
    raise ValueError()

