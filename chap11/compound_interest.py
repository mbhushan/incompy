import pylab


def compoundInterest(principal, rate, years):
    values = []

    for i in range(years+1):
        values.append(principal)
        principal += (principal * rate)
    pylab.plot(values)
    pylab.title('5% growth Compunded Annually')
    pylab.xlabel('Years of Compunding')
    pylab.ylabel('Value of Principal ($)')
    pylab.show()


def readInput():
    P = int(raw_input('Enter principal amount: '))
    R = float(raw_input('Enter rate: '))
    Y = int(raw_input('Enter years: '))
    return [P, R, Y]


def main():
    inp = readInput()
    print inp
    compoundInterest(inp[0], inp[1], inp[2])


if __name__ == '__main__':
    main()
