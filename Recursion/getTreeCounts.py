from fc_utils import Tree

def getTreeCounts(t):
    res = [0] * 6
    def getTreeCountsHelper(t):
        if t.isLeaf():
            res[t.getValue()] += 1
        else:
            for child in t.getChildren():
                getTreeCountsHelper(child)
            res[t.getValue()] += 1
    getTreeCountsHelper(t)
    return res

def testGetTreeCounts():
    t1 = Tree(4,
              Tree(2),
              Tree(1),
              Tree(4, Tree(0)))
    assert(getTreeCounts(t1) == [1, 1, 1, 0, 2, 0])

testGetTreeCounts()