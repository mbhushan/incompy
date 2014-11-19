from int_to_str import intToStr


def addDigits(n):
    str_rep = intToStr(n)
    val = 0

    for c in str_rep:
        val += int(c)

    return val

n = int(raw_input('enter integer: '))

sum_digits = addDigits(n)

print 'sum of digits of {} is: {}'.format(n, sum_digits)
