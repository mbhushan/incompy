

def minkowskiDist(v1, v2, p):
    """ Assumes v1 and v2 are equal length arrays of numbers
    Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1.0/p)


def main():
    rattlesnake = [1, 1, 1, 1, 0]
    boaConstrictor = [0, 1, 0, 1, 0]
    dartFrog = [1, 0, 1, 0, 4]
    md = minkowskiDist(rattlesnake, boaConstrictor, 2)
    print "Minkowski distance between rattle snake and\
        boa constrictor:{}".format(round(md, 3))
    md = minkowskiDist(dartFrog, boaConstrictor, 2)
    print "Minkowski distance between dart from and\
        boa constrictor:{}".format(round(md, 3))

if __name__ == '__main__':
    main()
