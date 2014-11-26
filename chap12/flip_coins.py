import random


def flip(numFlips):
    headCount = 0

    for i in range(numFlips):
        if random.random() < 0.5:
            headCount += 1
    return float(headCount)/numFlips


def flipCoins(numFlipsPerTrial, numTrials):
    heads = []
    for i in range(numTrials):
        heads.append(flip(numFlipsPerTrial))
    mhead = sum(heads)/len(heads)

    return mhead


def readInput():
    numTrials = int(raw_input('Enter number of trials for experiment: '))
    numFlipsPerTrial = int(raw_input('Number of coin flips per trial: '))

    return (numFlipsPerTrial, numTrials)


def main():
    params = readInput()
    result = flipCoins(params[0], params[1])
    print 'Mean of Fraction of heads: ', result

if __name__ == '__main__':
    main()
