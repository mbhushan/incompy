# Check if the entered number is even or odd


def evenOdd(x):
    flag = 0
    if x % 2 == 1:
        flag = 1
    return flag

while True:
    try:
        num = int(raw_input("Enter number: "))
        break
    except ValueError:
        print 'Invalid Number!! Try again ...'

ans = evenOdd(num)
if ans == 0:
    print "{0} is EVEN!".format(num)
else:
    print "{0} is ODD!".format(num)
