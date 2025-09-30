from collections import deque

################################################################################
# BFS: Print nodes in breadth-first order visited
################################################################################

def bfs(graph, startNode):
    toVisit = deque([startNode])
    visited = [startNode]
    while len(toVisit) > 0:
        currNode = toVisit.popleft()
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                visited.append(neighbor)
                toVisit.append(neighbor)
    return visited

def bfs(graph, startNode):
    toVisit = deque([startNode])
    visited = []
    while len(toVisit) > 0:
        currNode = toVisit.popleft()
        if currNode not in visited:
            visited.append(currNode)
            for neighbor in graph[currNode]:
                toVisit.append(neighbor)
    return visited

def testBFS():
    print('Testing bfs()...', end=' ')

    graph = {
        'A' : ['B', 'D', 'F'],
        'B' : ['C', 'D', 'E'],
        'C' : ['A', 'D'],
        'D' : ['A'],
        'E' : [],
        'F' : ['D', 'E'],
    }
    assert(bfs(graph, 'A') == ['A', 'B', 'D', 'F', 'C', 'E'])
    assert(bfs(graph, 'B') == ['B', 'C', 'D', 'E', 'A', 'F'])
    assert(bfs(graph, 'C') == ['C', 'A', 'D', 'B', 'F', 'E'])
    assert(bfs(graph, 'D') == ['D', 'A', 'B', 'F', 'C', 'E'])
    assert(bfs(graph, 'E') == ['E'])
    assert(bfs(graph, 'F') == ['F', 'D', 'E', 'A', 'B', 'C'])

    print('Passed!')

testBFS()