#coding:UTF-8
import math

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

def dis_chebyshev(A, B):
    """chebyshev distance
    """
    if len(A) != len(B):
        return -1

    tmp = []
    length = len(A)
    for i in xrange(length):
        tmp.append(math.fabs(A[i]-B[i]))
    tmp.sort()
    return tmp[-1]

if __name__ == "__main__":
    print dis_manhattan([1,2,3],[4,5,6])
    print dis_euclidean([1,2,3],[4,5,6])
    print dis_chebyshev([1,2,3],[6,5,4])
