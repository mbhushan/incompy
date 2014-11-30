

def collisionProb(n, k):
    ''' assumption is k < n with k & n being positive integers'''
    prob = 1.0
    for r in range(1, k):
        prob *= (n-r)/float(n)
    return (1.0 - prob)


def readInput():
    n = int(raw_input('Enter N: '))
    k = int(raw_input('Enter K: '))
    return (n, k)


def main():
    n, k = readInput()
    prob = collisionProb(n, k)
    print "Collision probability is: {}".format(round(prob, 3))

if __name__ == '__main__':
    main()
