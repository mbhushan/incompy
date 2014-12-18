

def fastFib(n, memo={}):
    ''' Assumes n is int > 0, memoization used only by recrusive calls
    returns fibonacci of n '''
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result


def main():
    n = int(raw_input("Enter positive integer: "))
    f = fastFib(n)
    print "Fibonacci of {} is: {}".format(n, f)


if __name__ == '__main__':
    main()
