import random
import pylab


def successfulStarts(eventProb, trials):
    """Assumes eventProb is a float representing a probability
    of a single attempt being successful. numTrials a positive int
    Returns a list of the number of attempts needed before a
    success for each trial."""
    triesB4Success = []
    for t in range(trials):
        consecFails = 0
        while random.random() > eventProb:
            consecFails += 1
        triesB4Success.append(consecFails)
    return triesB4Success


def plotDist(D, successProb, trials):
    pylab.hist(D, bins=20)
    pylab.xlabel("Tries before success")
    pylab.ylabel("Occurances out of " + str(trials) + " trials")
    pylab.title("Probability of starting each try: " + str(successProb))
    pylab.plot()
    pylab.show()


def readInput():
    successProb = float(raw_input("Enter success probability: "))
    trials = int(raw_input("Enter number of trials: "))

    return (successProb, trials)


def main():
    successProb, trials = readInput()
    D = successfulStarts(successProb, trials)
    plotDist(D, successProb, trials)


if __name__ == '__main__':
    main()
