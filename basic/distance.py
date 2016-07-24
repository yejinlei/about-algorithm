#coding:UTF-8
import math

def dis_euclidean(A, B):
    """euclidean distance
    """
    if len(A) != len(B):
        return -1

    res = 0
    length = len(A)
    for i in xrange(length):
        res += (A[i]-B[i])*(A[i]-B[i])
    return math.sqrt(res)

def dis_manhattan(A, B):
    """manhattan distance
    """
    if len(A) != len(B):
        return -1

    res = 0
    length = len(A)
    for i in xrange(length):
        res += math.fabs(A[i]-B[i])
    return res

if __name__ == "__main__":
    print dis_euclidean([1,2,3],[4,5,6])
    print dis_manhattan([1,2,3],[4,5,6])