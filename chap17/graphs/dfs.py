# DFS implemetation on the graph

from digraph import Digraph
from node_edge import Edge


def printPath(path):
    """ Assumes path is a list of nodes """
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path)-1:
            result = result + "->"
    return result


def dfs(graph, start, end, path, shortest):
    """Assumes graph is a Digraph; start and end are nodes;
    path and shortest are lists of nodes-Returns a shortest path
    from start to end in graph"""
    path = path + [start]
    print "current dfs path: ", printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        # avoids cycle
        if node not in path:
            if not shortest or len(path) < len(shortest):
                newPath = dfs(graph, node, end, path, shortest)
                if newPath:
                    shortest = newPath
    return shortest


def search(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph"""
    return dfs(graph, start, end, [], None)


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
    print "Shortest path by DFS: ", printPath(sp)


def main():
    testSP()


if __name__ == '__main__':
    main()
