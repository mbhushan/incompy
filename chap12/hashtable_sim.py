import random


def simInsertions(indices, insertions):
    """Assumes numIndices and numInsertions are positive ints.
    Returns 1 if there is a collision; 0 otherwise"""
    choices = range(indices)
    used = []
    for i in range(insertions):
        hashVal = random.choice(choices)
        if hashVal in used:
            return 1
        else:
            used.append(hashVal)
    return 0


def findProb(indices, insertions, trials):
    collisions = 0.0
    for t in range(trials):
        collisions += simInsertions(indices, insertions)
    return collisions/trials


def readInput():
    indices = int(raw_input('Enter number of hashBuckets: '))
    insertions = int(raw_input('Enter number of insertions: '))
    trials = int(raw_input('Number of trials: '))
    return (indices, insertions, trials)


def main():
    ind, ins, trials = readInput()
    prob = findProb(ind, ins, trials)
    print 'Probability of a collision: {}'.format(round(prob, 4))


if __name__ == '__main__':
    main()
