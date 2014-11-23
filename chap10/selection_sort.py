# Selection sort algorithm


def selSort(L):
    ''' Assumes L is a list of elements that can be comparated
    using >. And we sort L in ascending order '''
    if L is None or len(L) <= 1:
        return L

    suffixIndex = 0
    lenL = len(L)
    while suffixIndex != lenL:
        for i in range(suffixIndex, lenL):
            if L[i] < L[suffixIndex]:
                L[suffixIndex], L[i] = L[i], L[suffixIndex]
        suffixIndex += 1
    return L


def readInput():
    S = raw_input('Enter space separated list of integers: ')
    S = S.split(" ")
    result = [int(i) for i in S]
    return result


def main():
    L = readInput()
    sortedList = selSort(L)

    print 'Sorted List:'
    print sortedList
if __name__ == '__main__':
    main()
