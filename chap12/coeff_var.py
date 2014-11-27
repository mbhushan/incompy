# api for coefficient of variation
import numpy


def coeffVar(X):
    mean = sum(X)/float(len(X))
    try:
        return numpy.std(X)/mean
    except ZeroDivisionError:
        return float('nan')


def readInput():
    print 'Enter space separated list of numbers: '
    S = raw_input()
    S = S.split(" ")
    return [int(n) for n in S]


def main():
    X = readInput()
    cv = coeffVar(X)
    print 'Coefficient Variation: ', round(cv, 4)

if __name__ == '__main__':
    main()
