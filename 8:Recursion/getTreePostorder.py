from fc_utils import Tree

def getTreePostorder(tree):
    if tree.isLeaf():
        return [tree.getValue()]
    else:
        res = []
        for child in tree.getChildren():
            res.extend(getTreePostorder(child))
        res.append(tree.getValue())
        return res

def testGetTreePostorder():
    '''
             ┌─── 2 
    ─── 1 ───┤
             └─── 3 
    '''
    t1 = Tree(1,
              Tree(2),
              Tree(3)
             )
    assert(getTreePostorder(t1) == [2, 3, 1])

    '''
    ─── 4 ─────── 5
    '''
    t2 = Tree(4,
              Tree(5),
             )
    assert(getTreePostorder(t2) == [5, 4])

    '''
                       ┌─── 2 
             ┌─── 1 ───┤
    ─── 6 ───┤         └─── 3 
             │
             └─── 4 ─────── 5 
    '''
    t3 = Tree(6,
              Tree(1,
                   Tree(2),
                   Tree(3)
                  ),
              Tree(4,
                   Tree(5),
                  )
             )
    assert(getTreePostorder(t3) == [2, 3, 1, 5, 4, 6])

    '''
             ┌─── 2 ─────── x ─────── 8 
             │
             ├─── 3 
    ─── 1 ───┤
             │         ┌─── 6 
             └─── y ───┤
                       └─── z 
    '''
    t4 = Tree(1,
              Tree(2,
                   Tree('x',
                        Tree(8)
                       )
                  ),
              Tree(3),
              Tree('y',
                   Tree(6),
                   Tree('z')
                  )
             )
    assert(getTreePostorder(t4) == [8, 'x', 2, 3, 6, 'z', 'y', 1])

    '''
    ─── 0
    '''
    t5 = Tree(0)
    assert(getTreePostorder(t5) == [0])

    print("Passed sample test cases!")

def main():
    testGetTreePostorder()

main()