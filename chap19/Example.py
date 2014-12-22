from minkowski_dist import minkowskiDist


class Example(object):

    def __init__(self, name, features, label=None):
        # Assumes features is an array of numbers
        self.name = name
        self.features = features
        self.label = label

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def getLabel(self):
        return self.label

    def getDimensionality(self):
        return len(self.features)

    def getDistance(self, other):
        return minkowskiDist(self.features, other.getFeatures(), 2)

    def __str__(self):
        return self.name + ":" + str(self.features) + ":" + str(self.label)
