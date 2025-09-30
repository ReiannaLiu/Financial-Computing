from fc_utils import BST

def closestValue(bst, k):
    if bst == None:
        return float("inf")
    elif bst == k:
        return k
    else:
        candidate1 = bst.getValue()
        if k < candidate1:
            candidate2 = closestValue(bst.getLeft(), k)
        else:
            candidate2= closestValue(bst.getRight(), k)
        return candidate1 if abs(candidate1 - k) < abs(candidate2 - k) else candidate2

def testClosestValue():
    '''
             ┌─── 1 ─────── 3 
             │
    ─── 4 ───┤         ┌─── 5 
             └─── 8 ───┤
                       └─── 10 
    '''
    bst = BST.fromList([4, 8, 10, 1, 5, 3])
    assert(closestValue(bst, 6) == 5)
    assert(closestValue(bst, 20) == 10)
    assert(closestValue(bst, -1) == 1)
    assert(closestValue(bst, 5) == 5)
    assert(closestValue(bst, 2) in [1, 3])

    '''
               ┌─── -20 ─────── -15 
    ─── -10 ───┤
               └─── -3 ──────── -7 
    '''
    bst = BST.fromList([-10, -20, -3, -7, -15])
    assert(closestValue(bst, -8) == -7)
    assert(closestValue(bst, -13) == -15)
    assert(closestValue(bst, -3) == -3)
    assert(closestValue(bst, 0) == -3)
    assert(closestValue(bst, -5) in [-3, -7])

    '''
    ─── 5
    '''
    bst = BST.fromList([5])
    assert(closestValue(bst, 5) == 5)
    assert(closestValue(bst, 100) == 5)
    assert(closestValue(bst, -3) == 5)

def main():
    testClosestValue()

main()