# Iterative and recursive variant of factorial programs


def factI(n):
    ''' assumes that n is an int > 0  returns n!'''
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def factR(n):
    ''' assumes that n is an int > 0  returns n!'''
    if n == 1:
        return n
    else:
        return n * factR(n-1)

n = int(raw_input('Enter Integer: '))
facti = factI(n)
factr = factR(n)
print 'Iterative {0}! is: {1}'.format(n, facti)
print 'Recursive {0}! is: {1}'.format(n, factr)
