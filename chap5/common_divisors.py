# find common divisors of 2 numbers and print the sums of the divisors as well


def findDivisors(x, y):
    ''' Assumes x & y are positive ints > 0
    Returns a tuple containing all common divisors of x & y '''

    divisors = ()
    for n in range(1, min(x, y) + 1):
        if x % n == 0 and y % n == 0:
            divisors = divisors + (n, )
    return divisors

x = int(raw_input('Enter x: '))
y = int(raw_input('Enter y: '))

divisors = findDivisors(x, y)

print 'Common divisors of {} and {} are: '.format(x, y)
print divisors

sum = 0
for d in divisors:
    sum += d

print 'Sum of all divisors is: {}'.format(sum)
