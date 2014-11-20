# find the intersection of lists L1 & L2


def intersect(L1, L2):
    tmp = []
    for x in L1:
        for y in L2:
            if x == y:
                tmp.append(x)
    # Build a list without duplicates
    result = []
    for i in tmp:
        if i not in result:
            result.append(i)
    return result

s1 = raw_input('Enter list L1: ')
s2 = raw_input('Enter list L2: ')

L1 = s1.split(",")
L2 = s2.split(",")

result = intersect(L1, L2)

print 'intersection: ', result
