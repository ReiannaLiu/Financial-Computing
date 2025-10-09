def partition(L):
    pivot = L[0]
    left, right = [], []
    for i in range(1, len(L)):
        if L[i] <= pivot:
            left.append(L[i])
        else:
            right.append(L[i])
    return left, pivot, right

def quickSort(L):
    if len(L) < 2:
        return L
    else:
        left, pivot, right = partition(L)
        return quickSort(left) + [pivot] + quickSort(right)

def testPartition():
    assert(partition([3,2,5,1,4]) == ([2,1], 3, [5,4]))
    assert(partition([3,2,3,1,4]) == ([2,3,1], 3, [4]))

def testQuickSort():
    L1 = [5,2,0,7,6,3,1,4]
    assert(quickSort(L1) == sorted(L1))
    L2 = [8,0,4,6,7,5,9,3,2,1]
    assert(quickSort(L2) == sorted(L2))

testPartition()
testQuickSort()