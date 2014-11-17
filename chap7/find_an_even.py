
def findAnEven(ilist):
    ''' Assumes ilist is a list of numbers.
    Returns the first even number in ilist
    Raises ValueError if ilist does not contain an even number '''
    for i in ilist:
        if i % 2 == 0:
            return i
    raise ValueError('No even numbers found!')

st = raw_input('Enter comma separated integers: ')

st = st.split(",")

ilist = []
for s in st:
    s = int(s)
    ilist.append(s)

ans = findAnEven(ilist)

print 'First even in the list is: ', ans
