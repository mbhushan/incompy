# Given a list compute all combination of the elements of L and return
# list of lists.


def getBinaryRep(n, digits):
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    if len(result) > digits:
        raise ValueError('not enough digits!')
    for i in range(digits - len(result)):
        result = '0' + result
    return result


def getPowerSet(L):
    powerset = []

    for i in range(0, 2**len(L)):
        bin_rep = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if bin_rep[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

st = raw_input('enter comma separated list of numbers: ')
L = st.split(",")

ans = getPowerSet(L)

print 'Power Set of the input is: '
print ans
