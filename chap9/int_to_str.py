
def intToStr(i):
    ''' Assumes i is a nonnegative int, returns a string rep of i '''
    digits = '0123456789'

    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i//10
    return result

n = int(raw_input('Enter integer: '))

st = intToStr(n)

print 'string rep of {} is: \"{}\"'.format(n, st)
