import pylab


class Cluster(object):

    def __init__(self, examples, exampleType):
        """Assumes examples is alist of type exampleType"""
        self.examples = examples
        self.exampleType = exampleType
        self.centroid = self.computeCentroid()

    def update(self, examples):
        """replace the examples in the cluster with the new examples
        Return how much the centroid has changed!"""
        oldCentroid = self.centroid
        self.examples = examples
        if len(examples) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0

    def members(self):
        for e in self.examples:
            yield e

    def size(self):
        return len(self.examples)

    def getCentroid(self):
        return self.centroid

    def computeCentroid(self):
        dim = self.examples[0].getDimensionality()
        totVals = pylab.array([0.0]*dim)
        elen = self.examples
        for e in self.examples:
            totVals += e.getFeatures()
        centroid = self.exampleType("centroid", totVals/float(elen))
        return centroid

    def variance(self):
        toDist = 0.0
        for e in self.examples:
            toDist += (e.getDistance(self.centroid))**2
        return toDist**0.5

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = "Cluster with centroid: "\
            + str(self.centroid.getFeatures()) + " contains: \n"
        for e in names:
            result += e + ", "
        return result[:-2]
