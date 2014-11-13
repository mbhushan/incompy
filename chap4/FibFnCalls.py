# Check and count the number of fibonacci calls for a given n


def fib(n):
    global fibcalls
    fibcalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(raw_input('Enter integer: '))

fibcalls = 0
result = fib(n)
print '{} fibonacci number is: {} with {} function\
 calls'.format(n, result, fibcalls)
