import random
import numpy


def throwNeedles(numNeedles):
    inCircle = 0
    for needles in xrange(1, numNeedles+1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    # multiplying by 4 (area of the square) - and curr we counting needls
    # in 1 quadrant only.
    return 4*(inCircle/float(numNeedles))


def getEstimate(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    currEst = sum(estimates)/len(estimates)
    print "Est. = " + str(round(currEst, 5)) + \
        ", Std. Dev. = " + str(round(sDev, 5))\
        + ", Needles = " + str(numNeedles)
    return (currEst, sDev)


def estimatePI(precision, numTrials, numNeedles):
    sDev = precision

    while sDev >= precision/2.0:
        currEst, sDev = getEstimate(numNeedles, numTrials)
        numNeedles *= 2
    return currEst


def readInput():
    precision = float(raw_input("Enter precision value: "))
    numTrials = int(raw_input("Enter number of trials: "))
    numNeedles = int(raw_input("Enter number of needles: "))
    return (precision, numTrials, numNeedles)


def main():
    precision, numTrials, numNeedles = readInput()
    estimatePI(precision, numTrials, numNeedles)


if __name__ == '__main__':
    main()
