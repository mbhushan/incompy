from node_edge import Edge
from digraph import Digraph


def printPath(path):
    """ Assumes path is a list of nodes """
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path)-1:
            result = result + "->"
    return result


def bfs(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQ = [initPath]
    while len(pathQ) != 0:
        # Get and remove oldest element from pathQ
        tmpPath = pathQ.pop()
        print 'Current BFS path: ', printPath(tmpPath)
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQ.append(newPath)
    return None


def search(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph"""
    return bfs(graph, start, end)


def testSP():
    nodes = []
    for name in range(6):
        nodes.append(str(name))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    sp = search(g, nodes[0], nodes[5])
    print "Shortest path by BFS: ", printPath(sp)


def main():
    testSP()


if __name__ == '__main__':
    main()
