# binary search implementation on a list.


def binarySearch(L, key):
    if L is None:
        return False
    L.sort()
    low = 0
    high = len(L)-1
    return binarySearchRec(L, low, high, key)


def binarySearchRec(L, low, high, key):
    if low > high:
        return False

    mid = low + (high-low)/2

    if L[mid] == key:
        return True
    elif key < L[mid]:
        return binarySearchRec(L, low, mid-1, key)
    else:
        return binarySearchRec(L, mid+1, high, key)


def binarySearchIter(L, low, high, key):
    mid = low + (high-low)/2

    while low <= high:
        mid = low + (high-low)/2
        if L[mid] == key:
            return True
        elif key < L[mid]:
            high = mid-1
        else:
            low = mid+1
    return False


L = raw_input('Enter comma separated list: ')
L = L.split(",")

key = raw_input('Enter key to be searched: ')

ans = binarySearch(L, key)

print 'is key {} present in list? {}'.format(key, ans)
