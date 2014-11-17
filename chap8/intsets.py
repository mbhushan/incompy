class IntSet(object):
    ''' An IntSet is a set of integers '''
    def __init__(self):
        ''' creates an empty set of integers '''
        self.vals = []

    def insert(self, e):
        ''' Assumes e is an integer and inserts e into self '''
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        ''' Assumes e is integer
        Returns True if e is in self, False otherwise '''
        return e in self.vals

    def remove(self, e):
        ''' Assumes e is integer, removes e from self
        Raises ValueError if e is not in self '''
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found!')

    def getMembers(self):
        ''' Returns a list of elements in self
        Nothing can be assumed about the order of elements. '''
        return self.vals[:]

    def __str__(self):
        ''' Returns a string representation of the self '''
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ","
        return '{' + result[:-1] + '}'  # -1 ommits the last comma

S = IntSet()
for i in range(1, 9):
    S.insert(i)

print "Members: {}".format(S.__str__())

n = int(raw_input('which element to remove: '))
S.remove(n)
print "Removed: ", n
print "Members: {}".format(S.__str__())
