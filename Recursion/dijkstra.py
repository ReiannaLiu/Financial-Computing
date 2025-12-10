from fc_utils import PQ
import heapq

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

def weightedDistances(graph, startNode):
    distances = {node : float('inf') for node in graph}
    distances[startNode] = 0
    toVisit = []
    heapq.heappush(toVisit, (0, startNode))

    while len(toVisit) > 0:
        currDist, currNode = heapq.heappop(toVisit)
        
        if currDist > distances[currNode]:
            continue

        for neighbor, weight in graph[currNode].items():
            neighborDist = weight + currDist
            if neighborDist < distances[neighbor]:
                distances[neighbor] = neighborDist
                heapq.heappush(toVisit, (neighborDist, neighbor))
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
    assert(weightedDistances(graph, 'S') == {'S': 0, 'A': 1, 'B': 3, 'C': 4, 'D': 7, 'E': float('inf')})
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

def dijkstra(graph, startNode):
    distances = {node : float('inf') for node in graph}
    distances[startNode] = 0
    parents = {node : None for node in graph}
    toVisit = [(0, startNode)]

    while len(toVisit) > 0:
        currDist, currNode = heapq.heappop(toVisit)

        if currDist > distances[currNode]:
            continue
        
        for neighbor, weight in graph[currNode].items():
            distToNeighbor = currDist + weight
            if distToNeighbor < distances[neighbor]:
                distances[neighbor] = distToNeighbor
                toVisit.append((distToNeighbor, neighbor))
                parents[neighbor] = currNode
    
    return reconstructPath(parents, startNode)


def reconstructPath(parents, start):
    paths = {node : None for node in parents}
    paths[start] = [start]
    for node, parent in parents.items():
        if parent == None:
            continue 

        currNode = node 
        path = []
        while currNode != None:
            path.append(currNode)
            if currNode == start:
                break
            currNode = parents[currNode]
        path.reverse()
        paths[node] = path
    return paths


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