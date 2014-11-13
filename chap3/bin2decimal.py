# given binary number print its decimal equivalent


def toDecimal(bin):
    # reverse the bin string
    bin = bin[::-1]
    dec = 0
    index = 0
    for i in bin:
        i = int(i)
        dec = dec + i*(2**index)
        index += 1
    return dec


bin = raw_input('Enter binary string: ')
dec = toDecimal(bin)

print 'Decimal number: ', dec
