from fc_utils import Tree

def dfs(t, v):
    if t.getValue() == v:
        return True
    else:
        for child in t.getChildren():
            if dfs(child, v):
                return True
        return False

def testDFS():
    print('Testing dfs()...', end=' ')
    t1 = Tree(1,
              Tree(2,
                   Tree(5,
                        Tree(8))),
              Tree(3),
              Tree(4,
                   Tree(6),
                   Tree(7)))
    assert(dfs(t1, 1) == True)
    assert(dfs(t1, 2) == True)
    assert(dfs(t1, 5) == True)
    assert(dfs(t1, 7) == True)
    assert(dfs(t1, 8) == True)
    
    assert(dfs(t1, 9) == False)
    assert(dfs(t1, 12) == False)
    assert(dfs(t1, -1) == False)
    
    t2 = Tree(4,
              Tree(5))
    
    assert(dfs(t2, 4) == True)
    assert(dfs(t2, 5) == True)
    
    assert(dfs(t2, 1) == False)
    assert(dfs(t2, 8) == False)
    
    t3 = Tree(6,
              Tree('a',
                   Tree('b'),
                   Tree('c')),
              Tree(4,
                   Tree(5)))

    assert(dfs(t3, 6) == True)
    assert(dfs(t3, 'a') == True)
    assert(dfs(t3, 'b') == True)
    assert(dfs(t3, 'c') == True)
    assert(dfs(t3, 4) == True)
    assert(dfs(t3, 5) == True)
    
    assert(dfs(t3, "s") == False)
    assert(dfs(t3, 12) == False)
    assert(dfs(t3, -1) == False)
    
    print("Passed!")

testDFS()