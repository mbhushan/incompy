import random
import pylab


def playSeries(slen, teamProb):
    """ Assumes ngames to be an odd integer, teamProb would be float between
    0 and 1"""
    won = 0
    for g in range(slen):
        if random.random() <= teamProb:
            won += 1
    return (won > (slen//2))


def simSeries(prob, slen, ngames):
    probStep = 0.01
    fracWon = []
    probsList = []

    while prob <= 1.0:
        seriesWon = 0.0
        for g in range(ngames):
            if playSeries(slen, prob):
                seriesWon += 1
        fracWon.append(seriesWon/ngames)
        probsList.append(prob)
        prob += probStep

    pylab.plot(probsList, fracWon, linewidth=5)
    pylab.xlabel("Probability of Winning a game")
    pylab.ylabel("Probability of Winning a series")
    pylab.axhline(0.95)
    pylab.ylim(0.5, 1.1)
    pylab.title(str(ngames) + " " + str(slen) + "-Game Series")
    pylab.show()


def readInput():
    try:
        prob = float(raw_input("probability of winning a game: "))
        seriesLen = int(raw_input("Game series length: "))
        numGames = int(raw_input("Number of series games: "))
        return (prob, seriesLen, numGames)
    except:
        print ' entered value is not numeric, please try again!'
        readInput()


def main():
    p, slen, ngames = readInput()
    simSeries(p, slen, ngames)

if __name__ == '__main__':
    main()
