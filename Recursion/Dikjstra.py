import heapq

def weightedDistances(graph, source):
    distance = {node : None for node in graph}
    toVisit = []
    heapq.heappush(toVisit, (0, source))
    while len(toVisit) > 0:
        currDist, currNode = heapq.heappop(toVisit)
        if distance[currNode] == None:
            distance[currNode] = currDist
            for neighbor, weight in graph[currNode].items():
                heapq.heappush(toVisit, (currDist + weight, neighbor))
    return distance
        
    
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
    print("Passed!")

testWeightedDistances()

####################################################################
def getPaths(parents, source):
    paths = {node : None for node in parents}
    paths[source] = source
    for node, parent in parents.items():
        if parent == None:
            continue
        path = []
        currNode = node
        while currNode != None:
            path.append(currNode)
            currNode = parents[currNode]
        paths[node] = list(reversed(path))
    return paths

def dijkstra(graph, source):
    distance = {node : None for node in graph}
    parents = {node : None for node in graph}
    toVisit = []
    heapq.heappush(toVisit, (0, source, None))
    while len(toVisit) > 0:
        currDist, currNode, parent = heapq.heappop(toVisit)
        if parents[currNode] == None:
            parents[currNode] = parent
            distance[currNode] = currDist
            for neighbor, weight in graph[currNode].items():
                heapq.heappush(toVisit, (currDist + weight, neighbor, currNode))
    return getPaths(parents, source)

def testDijkstra():
    graph = {
        'S' : {'A' : 1, 'C' : 5},
        'A' : {'B' : 2},
        'B' : {'C' : 1, 'D' : 5},
        'C' : {'D' : 3},
        'D' : {},
        'E' : {'D' : 2}
    }
    assert(dijkstra(graph, 'S') == {'S': 'S', 'A': ['S', 'A'], 'B': ['S', 'A', 'B'], 'C': ['S', 'A', 'B', 'C'], 'D': ['S', 'A', 'B', 'C', 'D'], 'E': None})

    graph = {
        'S' : {'A' : 1, 'C' : 5},
        'A' : {'B' : 2},
        'B' : {'C' : 1, 'D' : 5},
        'C' : {'D' : 3},
        'D' : {},
        'E' : {'D' : 2},
        'F' : {'E' : 2}
    }
    assert(dijkstra(graph, 'S') == {'S': 'S', 'A': ['S', 'A'], 'B': ['S', 'A', 'B'], 'C': ['S', 'A', 'B', 'C'], 'D': ['S', 'A', 'B', 'C', 'D'], 'E': None, 'F': None})
    
    print("Passed!")

testDijkstra()