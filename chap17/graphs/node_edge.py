class Node(object):

    def __init__(self, name):
        ''' assumes name is a string '''
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):

    def __init__(self, src, dst):
        ''' assumes src and dst are nodes '''
        self.src = src
        self.dst = dst

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dst

    def __str__(self):
        return self.src.getName() + "->" + self.dst.getName()


class WeightedEdge(Edge):

    ''' Assumes src & dst are nodes, weight a float '''
    def __init__(self, src, dst, weight=1.0):
        self.src = src
        self.dst = dst
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + "->(" + str(self.weight) + ")->"\
            + self.dst.getName()
