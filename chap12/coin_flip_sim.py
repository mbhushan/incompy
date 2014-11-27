import pylab
import numpy
import random


def makePlot(xVals, yVals, title, xLabel, yLabel, style,
             logX=False, logY=False):
    """ Plots xVals & yVals with supplied titles, labels and style """
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()
    pylab.show()


def runTrial(numFlips):
    headCount = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            headCount += 1
    tailCount = numFlips - headCount

    return (headCount, tailCount)


def flipPlot1(mini, maxi, trials):
    '''Plot summaries of results of trials of 2**mini to 2**maxi coin flips'''
    xAxis = []
    ratioMeans, ratioSDs, diffMeans, diffSDs = [], [], [],  []

    for r in range(mini, maxi+1):
        xAxis.append(2**r)

    for flips in xAxis:
        ratios = []
        diffs = []
        for t in range(trials):
            hc, tc = runTrial(flips)
            ratios.append(hc/float(tc))
            diffs.append(abs(hc - tc))
        ratioMeans.append(sum(ratios)/float(trials))
        diffMeans.append(sum(diffs)/float(trials))
        ratioSDs.append(numpy.std(ratios))
        diffSDs.append(numpy.std(diffs))

    numTrialString = '(' + str(trials) + ' Trials!)'
    title = 'Mean Heads/Tails Ratios' + numTrialString
    makePlot(xAxis, ratioMeans, title, 'Number of Flips',
             'Mean Heads/Tails', 'bo', logX=True)

    title = 'Std Deviation Heads/Tails Ratios' + numTrialString
    makePlot(xAxis, ratioSDs, title, 'Number of Flips',
             'Standard Deviation', 'bo',
             logX=True, logY=True)


flipPlot1(4, 20, 20)
