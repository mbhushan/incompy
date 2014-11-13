# checks whether a string reads the same way backwards and forwards.


def isPalindrome(s):
    ''' Assumes s is str and returns True if s is palindrome '''
    def toChar(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters += c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChar(s))

st = raw_input('Enter string: ')

print '{} is palindrome? {}'.format(st, isPalindrome(st))
