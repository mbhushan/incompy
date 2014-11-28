import pylab
import numpy
import random


def flipCoin(flips):
    headCount = 0
    for i in range(flips):
        if random.random() < 0.5:
            headCount += 1
    return headCount/float(flips)


def flipSim(numFlips, trials):
    headFrac = []

    for t in range(trials):
        headFrac.append(flipCoin(numFlips))

    mean = sum(headFrac)/len(headFrac)
    sd = numpy.std(headFrac)
    return (headFrac, mean, sd)


def labelPlot(flips, trials, mean, sd):
    pylab.title(str(trials) + ' trials of ' + str(flips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax - xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)), size='x-large')


def makePlots(nflip1, nflip2, trials):
    val1, mean1, sd1 = flipSim(nflip1, trials)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    labelPlot(nflip1, trials, mean1, sd1)
    pylab.show()

    pylab.figure()
    val2, mean2, sd2 = flipSim(nflip2, trials)
    pylab.hist(val2, bins=20)
    pylab.xlim(xmin, xmax)
    labelPlot(nflip2, trials, mean2, sd2)
    pylab.show()

def readInput():
    flip1 = int(raw_input('Enter number of flips1: '))
    flip2 = int(raw_input('Enter number of flips2: '))
    trials = int(raw_input('Enter number of trials: '))

    return (flip1, flip2, trials)

def main():
    f1, f2, T = readInput()
    makePlots(f1, f2, T)

if __name__ == '__main__':
    main()

