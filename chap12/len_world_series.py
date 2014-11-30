from world_series import playSeries
import pylab


def findSeriesLength(teamProb):
    numSeries = 200
    maxLen = 2500
    step = 10

    def fracWon(teamProb, numSeries, seriesLen):
        won = 0.0
        for series in range(numSeries):
            if playSeries(seriesLen, teamProb):
                won += 1
        return won/numSeries

    winFrac = []
    xVals = []
    for seriesLen in range(1, maxLen, step):
        xVals.append(seriesLen)
        winFrac.append(fracWon(teamProb, numSeries, seriesLen))

    pylab.plot(xVals, winFrac, linewidth=5)
    pylab.xlabel("Length of Series")
    pylab.ylabel("Probability of winning a series")
    pylab.title(str(round(teamProb, 4)) + ' probability of team winning a game')
    # draw horizontal line at 0.95
    pylab.axhline(0.95)
    pylab.show()


def main():
    YanksProb = 0.636
    PhilsProb = 0.574
    teamProb = YanksProb/(YanksProb + PhilsProb)
    slen = findSeriesLength(teamProb)
    print "longest series to conclude better team: {}".format(slen)

if __name__ == '__main__':
    main()
