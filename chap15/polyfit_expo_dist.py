import math
import pylab


# define an arbitrary expoenential distribution
def f(x):
    return 3*(2**(1.2*x))


def createExpData(f, xvals):
    """Asssumes f is an exponential function of one argument
    xVals is an array of suitable arguments for f
    Returns array containing results of applying f to the
    elements of xVals"""
    yvals = []
    for i in range(len(xvals)):
        yvals.append(f(xvals[i]))
    return pylab.array(xvals), pylab.array(yvals)


def fitExpData(xvals, yvals):
    """Assumes xVals and yVals arrays of numbers such that
    yVals[i] == f(xVals[i])
    Returns a, b, base such that log(f(x), base) == ax + b"""
    logvals = []
    for y in yvals:
        logvals.append(math.log(y, 2.0))
    a, b = pylab.polyfit(xvals, logvals, 1)
    return a, b, 2.0


def makePlot():
    xvals, yvals = createExpData(f, range(10))
    pylab.plot(xvals, yvals, 'ro', label="Actual Values")

    a, b, base = fitExpData(xvals, yvals)
    predictedVals = []
    for x in xvals:
        predictedVals.append(base**(a*x + b))
    pylab.plot(xvals, predictedVals, label="Predicted Values")
    pylab.title("Fitting an exponential function")
    pylab.legend()
    pylab.show()

    # lets look for a value of x ie not in original data
    print "a: {}, b: {}, base: {}".format(a, b, base)
    x = 20
    print 'f({}) = {}'.format(x, f(20))
    print 'Predicted f({}) = {}'.format(x, base**(a*x + b))


def main():
    makePlot()


if __name__ == '__main__':
    main()
