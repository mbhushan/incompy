from craps_game import CrapsGame
import numpy


def crapsSim(handsPerGame, numGames):
    """Assumes handsPerGame and numGames are ints > 0
    Play numGames games of handsPerGame hands, and print results"""
    games = []

    # play number of games
    for t in xrange(numGames):
        c = CrapsGame()
        for i in xrange(handsPerGame):
            c.playHand()
        games.append(c)

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


def readInput():
    handsPerGame = int(raw_input("Hands per games: "))
    numGames = int(raw_input("Number of games: "))
    return (handsPerGame, numGames)


def main():
    handsPerGame, numGames = readInput()
    crapsSim(handsPerGame, numGames)

if __name__ == '__main__':
    main()
