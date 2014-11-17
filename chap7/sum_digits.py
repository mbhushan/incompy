
def sumDigits(s):
    ''' Assumes s is a string, Returns the sum of the decimal digits in s
    for example 'a2b3c' returns 5 '''
    if not s:
        return None

    sum = 0
    for c in s:
        if not c.isalpha():
            sum += int(c)
    return sum

st = raw_input("Enter alphanumeric string: ")

result = sumDigits(st)

print "sum of digits is: ", result
