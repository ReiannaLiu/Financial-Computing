def powerset(L):
    if L == []:
        return [[]]
    else:
        curr = L[-1]
        restSet = powerset(L[:-1])
        res = []
        for subset in restSet:
            res.append(subset)
            res.append(subset + [curr])
        return sorted(res)

def testPowerSet():
    # Make sure that your output list is sorted. 
    L = [1, 2, 3]
    output = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert(powerset(L) == sorted(output))

    L = [5, -8]
    output = [[], [-8], [5], [5, -8]]
    assert(powerset(L) == sorted(output))

    L = [-1]
    output = [[], [-1]]
    assert(powerset(L) == sorted(output))

    L = []
    assert(powerset(L) == [[]])

    print("Passed sample test cases!")

def main():
    testPowerSet()

main()