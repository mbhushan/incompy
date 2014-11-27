# give a list of numbers - calculate the standard deviation


def stdDev(X):
    ''' Assumes that X is a list of numbers - returns std dev of X '''
    if not X:
        return None

    mean = float(sum(X)/len(X))
    total = 0.0
    for n in X:
        total += (n-mean)**2

    return (total/len(X))**0.5


def readInput():
    print 'Enter list of space separated numbers'
    L = raw_input()
    L = L.split(" ")
    return [int(n) for n in L]


def main():
    X = readInput()
    sd = stdDev(X)
    print 'Standard Deviation: ', round(sd, 3)

if __name__ == '__main__':
    main()
