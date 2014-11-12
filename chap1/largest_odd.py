# given input of 3 numbers - x,y,z - find the largest odd
# if none of x,y,z are odd then it should print a msg to that effect


def largestOdd(xlist):
    lodd = None
    flag = 1
    for n in xlist:
        if (n % 2 == 1):
            if flag == 1:
                lodd = n
                flag = 0
            elif n > lodd:
                lodd = n
    return lodd

x = int(raw_input("Enter X: "))
y = int(raw_input("Enter Y: "))
z = int(raw_input("Enter Z: "))
xlist = [x, y, z]

result = largestOdd(xlist)

print 'Largest odd among {0}, {1}, {2} is: {3}'.format(x, y, z, result)
