#coding:UTF-8
import math

def dis_euclidean(A, B):
    """euclidean distance
    """
    res = -1
    if len(A) != len(B):    return res

    for ai in A:
        for bi in B:
            res += (ai-bi)*(ai-bi)
    return math.sqrt(res)

if __name__ == "__main__":
    print dis_euclidean([1,2,3],[1,2,3])