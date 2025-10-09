def merge(L, M):
    res = [ ]
    i = j = 0
    while i < len(L) or j < len(M):
        if j == len(M):
            useL = True
        elif i == len(L):
            useL = False
        else:
            useL = (L[i] < M[j])
        if useL:
            res.append(L[i])
            i += 1
        else:
            res.append(M[j])
            j += 1
    return res

def mergeSort(L):
    if len(L) < 2:
        return L
    else:
        i = len(L) // 2
        sortedLeftHalf = mergeSort(L[:i])
        sortedRightHalf = mergeSort(L[i:])
        return merge(sortedLeftHalf, sortedRightHalf)

def testMerge():
    assert(merge([2,5], [1,6]) == [1,2,5,6])
    assert(merge([1,2], [5,6]) == [1,2,5,6])
    assert(merge([1,2,6], [5]) == [1,2,5,6])
    assert(merge([1,2,5,6], []) == [1,2,5,6])

def testMergeSort():
    L1 = [5,2,0,7,6,3,1,4]
    assert(mergeSort(L1) == sorted(L1))
    L2 = [8,0,4,6,7,5,9,3,2,1]
    assert(mergeSort(L2) == sorted(L2))

testMerge()
testMergeSort()