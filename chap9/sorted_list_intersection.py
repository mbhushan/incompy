# find the intersection of 2 sorted lists


def getIntersection(A, B):
    x = len(A)
    y = len(B)

    i = 0
    j = 0
    result = []
    while i < x and j < y:
        if A[i] < B[j]:
            i = i + 1
        elif A[i] > B[j]:
            j = j + 1
        else:
            result.append(A[i])
            i = i + 1
            j = j + 1
    return result

A = raw_input('Enter first list - comma separated: ')
B = raw_input('Enter second list - comma separated: ')

A = A.split(",")
B = B.split(",")

ans = getIntersection(A, B)
print 'Intersection: ', ans
