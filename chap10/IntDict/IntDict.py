# class for Int dictionary


class IntDict(object):
    """ A dictionary with integer keys """

    def __init__(self, numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, dictKey, dictVal):
        """ Assumes dictKey is an integer - adds the key """
        hashBucket = self.buckets[dictKey % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))

    def getValue(self, dictKey):
        """ Assumes dictKey to be int, Returns entry associated with dictKey """
        hashBucket = self.buckets[dictKey % self.numBuckets]
        for k in hashBucket:
            if k[0] == dictKey:
                return k[1]
        return None

    def __str__(self):
        result = "{"
        for b in self.buckets:
            for e in b:
                result += str(e[0]) + ":" + str(e[1]) + ", "
        # omit the last comma
        return result[:-1] + "}"
