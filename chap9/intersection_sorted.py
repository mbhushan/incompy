# Find the intersection of 2 lists which are sorted
# expected complexity is linear or linear logarithmic
# ex: [1,2,2,3,3,3] & [1,1,2,2,2,3,3] -> [1,2,2,3,3]


def findIntersection(A, B):
    if A is None or B is None:
        return None

    lenA = len(A)
    lenB = len(B)

    lookup = {}
    if lenA <= lenB:
        for x in A:
            count = 0
            if x in lookup.keys():
                count = lookup[x]
            lookup[x] = count + 1
        return getIntersect(B, lookup)
    else:
        for y in B:
            count = 0
            if y in lookup:
                count = lookup[y]
            lookup[y] = count+1
        return getIntersect(A, lookup)


def getIntersect(C, lookup):
    result = []
    for n in C:
        if n in lookup.keys():
            result.append(n)
            count = lookup[n]
            count = count-1
            if count == 0:
                del lookup[n]
            else:
                lookup[n] = count
    return result

A = raw_input('Enter first list: ')
B = raw_input('Enter second list: ')

A = A.split(",")
B = B.split(",")

ans = findIntersection(A, B)

print 'Intersection: ', ans
