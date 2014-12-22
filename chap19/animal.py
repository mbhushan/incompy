import numpy
from minkowski_dist import minkowskiDist


class Animal(object):

    def __init__(self, name, features):
        """Assumes name is a string and features is a list"""
        self.name = name
        self.features = numpy.array(features)

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self, other):
        """ Assumes other an animal, Returns euclidean distance between
        feature vectors of self and other"""
        return minkowskiDist(self.getFeatures(), other.getFeatures(), 2)
