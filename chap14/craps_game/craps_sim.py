from craps_game import CrapsGame
import numpy
import time


def crapsSim(handsPerGame, numGames, flag=True):
    """Assumes handsPerGame and numGames are ints > 0
    Play numGames games of handsPerGame hands, and print results"""
    games = []

    start = time.time()
    # play number of games
    for t in xrange(numGames):
        c = CrapsGame()
        for i in xrange(handsPerGame):
            if not flag:
                c.playHand()
            else:
                c.playhandFast()
        games.append(c)
    end = time.time()
    # calculate statistics for each game
    pROIGame, dpROIGame = [], []
    for g in games:
        wins, losses = g.passResult()
        pROIGame.append((wins - losses)/float(handsPerGame))

        wins, losses, pushes = g.dpResults()
        dpROIGame.append((wins - losses)/float(handsPerGame))

    # produce and print summary
    meanROI = str(round((100 * sum(pROIGame)/numGames), 4)) + "%"
    sigma = str(round(100 * numpy.std(pROIGame), 4)) + "%"
    print "Pass: ", "Mean ROI = ", meanROI, " std dev = ", sigma

    meanROI = str(round((100 * sum(dpROIGame)/numGames), 4)) + "%"
    sigma = str(round(100 * numpy.std(dpROIGame), 4)) + "%"
    print "Don't Pass: ", "Mean ROI = ", meanROI, " std dev = ", sigma

    print "TIME ELASPED: ", (end-start)


def readInput():
    handsPerGame = int(raw_input("Hands per games: "))
    numGames = int(raw_input("Number of games: "))
    flag = int(raw_input("Fast implementation <1 or 0>: "))

    return (handsPerGame, numGames, flag)


def main():
    handsPerGame, numGames, flag = readInput()
    if flag == 1:
        crapsSim(handsPerGame, numGames, True)
    else:
        crapsSim(handsPerGame, numGames, False)

if __name__ == '__main__':
    main()
