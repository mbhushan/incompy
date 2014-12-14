# Items class with item attribs of name, value and weight


class Item(object):

    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getItemName(self):
        return self.name

    def getItemValue(self):
        return self.value

    def getItemWeight(self):
        return self.weight

    def __str__(self):
        result = "<" + self.name + ", " + str(self.value) + ", " +\
            str(self.weight) + ">"
        return result
