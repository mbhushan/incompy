import pylab


def makePlot():
    vals = []
    for i in range(10):
        vals.append(2**i)

    pylab.plot(vals, 'bo', label='Actual Points')
    Xvals = pylab.arange(10)
    a, b, c, d, e = pylab.polyfit(Xvals, vals, 4)
    Yvals = a*(Xvals**4) + b*(Xvals**3) + c*(Xvals**2) + d*(Xvals) + e
    pylab.plot(Yvals, 'bx', label='Predicted Points', markersize=20)
    pylab.title('Fitting y = 2**x')
    pylab.legend()
    pylab.show()


def main():
    makePlot()


if __name__ == '__main__':
    main()
