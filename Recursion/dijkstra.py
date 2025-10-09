from fc_utils import PQ

def weightedDistances(graph, startNode):
    distances = {node : None for node in graph}
    toVisit = PQ(lambda x: x[1])
    toVisit.push((startNode, 0))
    while not toVisit.isEmpty():
        currNode, currDist = toVisit.pop()
        if distances[currNode] == None:
            distances[currNode] = currDist
            for neighbor, weight in graph[currNode].items():
                toVisit.push((neighbor, currDist + weight))
    return distances


def testWeightedDistances():
    graph = {
        'S' : {'A' : 1, 'C' : 5},
        'A' : {'B' : 2},
        'B' : {'C' : 1, 'D' : 5},
        'C' : {'D' : 3},
        'D' : {},
        'E' : {'D' : 2}
    }
    assert(weightedDistances(graph, 'S') == {'S': 0, 'A': 1, 'B': 3, 'C': 4, 'D': 7, 'E': None})
    print("passed!")

testWeightedDistances()


####################################################################
def getPath(parents, startNode):
    paths = {node : None for node in parents}
    paths[startNode] = [startNode]
    for node, parent in parents.items():
        if parent == None:
            continue
        path, currNode = [], node
        while currNode != None:
            path.append(currNode)
            currNode = parents[currNode]
        paths[node] = list(reversed(path))
    return paths

def dijkstra(graph, startNode):
    distances = {node : None for node in graph}
    parents = {node : None for node in graph}
    toVisit = PQ(lambda x: x[1])
    toVisit.push((startNode, 0, None))
    while not toVisit.isEmpty():
        currNode, currDist, parent = toVisit.pop()
        if distances[currNode] == None:
            distances[currNode] = currDist
            parents[currNode] = parent
            for neighbor, weight in graph[currNode].items():
                toVisit.push((neighbor, currDist + weight, currNode))
    return getPath(parents, startNode)

def testDijkstra():
    graph = {
        'S' : {'A' : 1, 'C' : 5},
        'A' : {'B' : 2},
        'B' : {'C' : 1, 'D' : 5},
        'C' : {'D' : 3},
        'D' : {},
        'E' : {'D' : 2}
    }
    assert(dijkstra(graph, 'S') == {'S': ['S'], 'A': ['S', 'A'], 'B': ['S', 'A', 'B'], 'C': ['S', 'A', 'B', 'C'], 'D': ['S', 'A', 'B', 'C', 'D'], 'E': None})

    graph = {
        'S' : {'A' : 1, 'C' : 5},
        'A' : {'B' : 2},
        'B' : {'C' : 1, 'D' : 5},
        'C' : {'D' : 3},
        'D' : {},
        'E' : {'D' : 2},
        'F' : {'E' : 2}
    }
    assert(dijkstra(graph, 'S') == {'S': ['S'], 'A': ['S', 'A'], 'B': ['S', 'A', 'B'], 'C': ['S', 'A', 'B', 'C'], 'D': ['S', 'A', 'B', 'C', 'D'], 'E': None, 'F': None})
    print("passed!")

testDijkstra()