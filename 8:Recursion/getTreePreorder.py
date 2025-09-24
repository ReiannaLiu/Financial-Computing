from fc_utils import Tree

def getTreePreorder(tree):
    if tree.isLeaf():
        return [tree.getValue()]
    else:
        res = [tree.getValue()]
        for child in tree.getChildren():
            res.extend(getTreePreorder(child))
        return res

def testGetTreePreorder():
    '''
             ┌─── 2 ─────── 5 ─────── 8 
             │
             ├─── 3 
    ─── 1 ───┤
             │         ┌─── 6 
             └─── 4 ───┤
                       └─── 7 
    '''
    t1 = Tree(1,
              Tree(2,
                   Tree(5,
                        Tree(8)
                       )
                  ),
              Tree(3),
              Tree(4,
                   Tree(6),
                   Tree(7)
                  )
             )
    assert(getTreePreorder(t1) == [1, 2, 5, 8, 3, 4, 6, 7])

    '''
    ─── 4 ─────── 5 
    '''
    t2 = Tree(4,
              Tree(5),
             )
    assert(getTreePreorder(t2) == [4, 5])

    '''
                       ┌─── b 
             ┌─── a ───┤
    ─── 6 ───┤         └─── c 
             │
             └─── 4 ─────── 5
    '''
    t3 = Tree(6,
              Tree('a',
                   Tree('b'),
                   Tree('c')
                  ),
              Tree(4,
                   Tree(5),
                  )
             )
    assert(getTreePreorder(t3) == [6, 'a', 'b', 'c', 4, 5])

    '''
             ┌─── 2 
    ─── 1 ───┤
             └─── 3
    '''
    t4 = Tree(1,
              Tree(2),
              Tree(3)
             )
    assert(getTreePreorder(t4) == [1, 2, 3])

    '''
    ─── 0 
    '''
    t5 = Tree(0)
    assert(getTreePreorder(t5) == [0])

    print("Passed sample test cases!")

def main():
    testGetTreePreorder()

main()