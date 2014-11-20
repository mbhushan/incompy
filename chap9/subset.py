# Given 2 lists check if one of the list is subset of another.


def isSubset(L1, L2):
    for i in L1:
        matched = False
        for j in L2:
            if i == j:
                matched = True
        if not matched:
            return False
    return True

s1 = raw_input('Enter first list L1 of chars (comma separated): ')
s2 = raw_input('Enter second list L2 of chars (comma separated): ')
L1 = s1.split(",")
L2 = s2.split(",")

ans = isSubset(L1, L2)

print 'Is L1 a subset of L2 ? {}'.format(ans)
