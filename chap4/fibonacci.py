# evaluate fibonacci numbers


def fib(n):
    ''' Assumes n an int > 0 '''
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(raw_input('Enter integer: '))

for i in range(0, n+1):
    print 'fib of {}: {}'.format(i, fib(i))
