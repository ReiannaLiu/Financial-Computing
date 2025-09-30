from fc_utils import Tree

def maxBranchSum(tree):
    return maxBranchSumHelper(tree, 0, float("-inf"))

def maxBranchSumHelper(currNode, pathSum, maxSum):
    if currNode.isLeaf():
        return currNode.getValue() + pathSum
    else:
        pathSum += currNode.getValue()
        for child in currNode.getChildren():
            potentialSolns = maxBranchSumHelper(child, pathSum, maxSum)
            maxSum = max(maxSum, potentialSolns)
        return maxSum

def testMaxBranchSum():
    '''
                        ┌─── 8 
             ┌─── 5 ────┤
             │          └─── -3 
    ─── 1 ───┤
             │          ┌─── 40 
             └─── -9 ───┤
                        └─── 8 
    '''
    t = Tree(1,
             Tree(5,
                  Tree(8),
                  Tree(-3)),
             Tree(-9,
                  Tree(40),
                  Tree(8)))
    assert(maxBranchSum(t) == 32)   # 1 - 9 + 40 = 32

    '''
             ┌─── 3 
             │
    ─── 2 ───┼─── 100 ─────── 4 
             │
             └─── -5 ──────── 1000 
    '''
    t = Tree(2,
             Tree(3),
             Tree(100, Tree(4)),
             Tree(-5, Tree(1000)))
    assert(maxBranchSum(t) == 997)   # 2 - 5 + 100 = 997

    '''
               ┌─── -20 ─────── -1 
    ─── -10 ───┤
               └─── -30 
    '''
    t = Tree(-10,
             Tree(-20, Tree(-1)),
             Tree(-30))
    assert(maxBranchSum(t) == -31)  # -10 - 20 - 1 = -31

    '''
    ─── 5 ─────── 4 ─────── 3 ─────── 2 
    '''
    t = Tree(5, Tree(4, Tree(3, Tree(2))))
    assert(maxBranchSum(t) == 14)   # 5 + 4 + 3 + 2 = 14

def main():
    testMaxBranchSum()

main()