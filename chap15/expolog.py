import pylab


def makePlot():
    xvals, yvals = [], []
    for i in range(10):
        xvals.append(i)
        yvals.append(2**i)

    pylab.plot(xvals, yvals)
    pylab.semilogy()
    pylab.show()


def main():
    makePlot()

if __name__ == '__main__':
    main()
