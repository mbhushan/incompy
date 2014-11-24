import random
import IntDict


def main():
    D = IntDict.IntDict(29)
    for i in range(20):
        key = random.randint(0, 10**5)
        D.addEntry(key, i)
    print 'The value of the IntDict is: '
    print D
    print '\n', 'The buckets are: '
    for hashBucket in D.buckets:
        print ' ', hashBucket


if __name__ == '__main__':
    main()
