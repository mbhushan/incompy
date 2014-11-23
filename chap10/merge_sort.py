# Merge sort implementation
import operator


def merge(left, right, compare):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def mergeSort(L, compare=operator.lt):
    if len(L) < 2:
        return L
    else:
        mid = len(L)//2
        left = mergeSort(L[:mid], compare)
        right = mergeSort(L[mid:], compare)
        return merge(left, right, compare)


def readInput():
    print 'Enter space separated list of integers'
    S = raw_input()
    S = S.split(" ")
    return [int(i) for i in S]


def main():
    L = readInput()
    result = mergeSort(L)
    print 'Sorted list is: '
    print result


if __name__ == '__main__':
    main()
