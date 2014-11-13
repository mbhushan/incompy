# Write a function isIn that accepts two strings as arguments
# and returns True if either string occurs anywhere in the other, and False
# otherwise.


def isIn(x, y):
    if len(x) <= len(y):
        if x.find(y) > 0:
            return True
    else:
        if x.find(y) > 0:
            return True
    return False

str1 = raw_input('Enter first string: ')
str2 = raw_input('Enter second string: ')

print 'Either string occurs anywhere in the other? {}'.format(isIn(str1, str2))
