import pylab


def getTrajectory(filename):
    f = open(filename, 'r')
    distances = []
    h1, h2, h3, h4 = [], [], [], []
    f.readline()
    for line in f:
        d, ah, bh, ch, dh = line.split(",")
        distances.append(float(d))
        h1.append(float(ah))
        h2.append(float(bh))
        h3.append(float(ch))
        h4.append(float(dh))
    f.close()
    return (distances, [h1, h2, h3, h4])


def rSquared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
    predicted a one-dimensional array of predicted values
    Returns coefficient of determination"""
    estimatedError = ((predicted - measured)**2).sum()
    meanOfMeasured = measured.sum()/float(len(measured))
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimatedError/variability


def processTrajectories(filename):
    dist, heights = getTrajectory(filename)
    trials = len(heights)
    dist = pylab.array(dist)

    # get array combiming mean height at each distances
    totHeights = pylab.array([0] * len(dist))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    meanHeights = totHeights/len(heights)

    # start plotting :)
    pylab.title("Trajectile of Projectile " + "(Mean of " + str(trials)
                + " trails)")
    pylab.xlabel("Inches from launch point")
    pylab.ylabel("Inches above launch point")
    pylab.plot(dist, meanHeights, 'bo')

    a, b = pylab.polyfit(dist, meanHeights, 1)
    altitudes = a * dist + b
    pylab.plot(dist, altitudes, 'b', label='linear fit')
    print 'RSquared of linear fit: ', rSquared(meanHeights, altitudes)

    a, b, c = pylab.polyfit(dist, meanHeights, 2)
    altitudes = a*(dist**2) + b*(dist) + c
    pylab.plot(dist, altitudes, 'b:', label="Quadratic Fit")
    print 'RSquared of quadratic fit: ', rSquared(meanHeights, altitudes)
    pylab.legend()

    pylab.show()


def main():
    filename = "projdata.csv"
    processTrajectories(filename)

if __name__ == '__main__':
    main()
