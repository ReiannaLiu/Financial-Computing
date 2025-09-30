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

################################################################################
# DFS: Print nodes in depth-first order visited
################################################################################

def dfs(graph, startNode):
    return dfsHelper(graph, startNode, {startNode})

def dfsHelper(graph, startNode, visited):
    res = [startNode]
    for neighbor in graph[startNode]:
        if neighbor not in visited:
            visited.add(neighbor)
            res += dfsHelper(graph, neighbor, visited)
    return res

def testDFS():
    print('Testing dfs()...', end=' ')

    graph = {
        'A' : ['B', 'D', 'F'],
        'B' : ['C', 'D', 'E'],
        'C' : ['A', 'D'],
        'D' : ['A'],
        'E' : [],
        'F' : ['D', 'E'],
    }
    assert(dfs(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F'])
    assert(dfs(graph, 'B') == ['B', 'C', 'A', 'D', 'F', 'E'])
    assert(dfs(graph, 'C') == ['C', 'A', 'B', 'D', 'E', 'F'])
    assert(dfs(graph, 'D') == ['D', 'A', 'B', 'C', 'E', 'F'])
    assert(dfs(graph, 'E') == ['E'])
    assert(dfs(graph, 'F') == ['F', 'D', 'A', 'B', 'C', 'E'])

    print('Passed!')

testDFS()


################################################################################
# Iterative DFS: Print nodes in depth-first order visited
################################################################################

def iterativeDFS(graph, startNode):
    toVisit = [startNode]
    visited = []
    while len(toVisit) > 0:
        currNode = toVisit.pop()
        if currNode not in visited:
            visited.append(currNode)
            for neighbor in graph[currNode]:
                toVisit.append(neighbor)
    return visited

def testIterativeDFS():
    print('Testing iterativeDFS()...', end=' ')

    graph = {
        'A' : ['B', 'D', 'F'],
        'B' : ['C', 'D', 'E'],
        'C' : ['A', 'D'],
        'D' : ['A'],
        'E' : [],
        'F' : ['D', 'E'],
    }

    assert(iterativeDFS(graph, 'A') == ['A', 'F', 'E', 'D', 'B', 'C'])
    assert(iterativeDFS(graph, 'B') == ['B', 'E', 'D', 'A', 'F', 'C'])
    assert(iterativeDFS(graph, 'C') == ['C', 'D', 'A', 'F', 'E', 'B'])
    assert(iterativeDFS(graph, 'D') == ['D', 'A', 'F', 'E', 'B', 'C'])
    assert(iterativeDFS(graph, 'E') == ['E'])
    assert(iterativeDFS(graph, 'F') == ['F', 'E', 'D', 'A', 'B', 'C'])

    print('Passed!')

testIterativeDFS()