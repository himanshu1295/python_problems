# Given two sets A and B. check whether A is subset of B ?
# A is subset of B, if all elements of a set A are present in another set B.

A = {1, 4, 3}
B = {1, 4, 3, 2}

def CheckSubset(A, B):
    ans = A.issubset(B)      # this returns True if A is present in subset B
    print(ans)

CheckSubset(A, B)