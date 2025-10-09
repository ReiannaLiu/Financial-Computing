def hasSublistSum(L, s):
    if L == [] and s == 0:
        return True
    elif L == [] and s != 0:
        return False
    else:
        curr = L[0]
        return hasSublistSum(L[1:], s) or hasSublistSum(L[1:], s - curr)

def testHasSublistSum():
    L = [1, 6, 2, 8]
    assert(hasSublistSum(L, 3) == True) # 1 + 2 = 3

    L = [1, 6, 2, 8]
    assert(hasSublistSum(L, 11) == True) # 1 + 2 + 8 = 11

    L = [3, -1, 7]
    assert(hasSublistSum(L, -1) == True) # -1 = -1

    L = [7, -1, 4]
    assert(hasSublistSum(L, -5) == False) 
    
    L = [8, 1, 1]
    assert(hasSublistSum(L, 2) == True) # 1 + 1 = 2

    L = [8, 1]
    assert(hasSublistSum(L, 2) == False) 

    L = []
    assert(hasSublistSum(L, 0) == True)
        
    L = []
    assert(hasSublistSum(L, 1) == False)

def main():
    testHasSublistSum()

main()