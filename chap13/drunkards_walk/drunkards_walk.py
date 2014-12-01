from Field import Field
from Drunk import UsualDrunk
from Location import Location
import numpy


def coeffVar(X):
    mean = sum(X)/float(len(X))
    if round(mean, 2) < 0.02:
        return float('nan')
    try:
        return numpy.std(X)/mean
    except ZeroDivisionError:
        return float('nan')


def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
    Moves d numSteps times, and returns the difference between
    the final location and the location at the start of the walk."""
    start = f.getLoc(d)
    # print "Start: ", start
    for s in range(numSteps):
        f.moveDrunk(d)
    dist = start.distanceFrom(f.getLoc(d))
    # print "DIST: ", dist
    return dist


def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an int > 0,
    dClass a subclass of Drunk Simulates numTrials walks of numSteps steps each.
    Returns a list of the final distances for each trial"""
    Homer = dClass()
    origin = Location(0.0, 0.0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunks(Homer, origin)
        distances.append(walk(f, Homer, numSteps))
    return distances


def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints >= 0
    numTrials an int > 0, dClass a subclass of Drunk
    For each number of steps in walkLengths, runs simWalks with
    numTrials walks and prints results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print dClass.__name__, ' random walk of ', numSteps, ' steps'
        print "Mean = ", sum(distances)/len(distances), ' CV = ',\
            coeffVar(distances)
        print "Max = ", max(distances), " Min = ", min(distances)


def main():
    # drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
    drunkTest((0, 1), 100, UsualDrunk)
    drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)


if __name__ == '__main__':
    main()
