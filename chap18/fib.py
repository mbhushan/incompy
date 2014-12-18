
def fib(n):
    ''' assumes n is int >= 0, Returns Fibonacci of n '''
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def readInput():
    n = int(raw_input("Enter postive integer n: "))
    return n


def main():
    n = readInput()
    f = fib(n)
    print "Fibonacci of {} is: {}".format(n, f)


if __name__ == '__main__':
    main()
