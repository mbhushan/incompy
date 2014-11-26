import random
import pylab


def flipPlot(mini, maxi):
    ''' Assumes min, max as positive integer and min < max '''
    ratios = []
    diffs = []
    xAxis = []

    for i in range(mini, maxi+1):
        xAxis.append(2**i)

    for flips in xAxis:
        headCount = 0
        for f in range(flips):
            if random.random() < 0.5:
                headCount += 1
        tailCount = flips - headCount
        ratios.append(headCount/float(tailCount))
        diffs.append(abs(headCount - tailCount))
    pylab.title("Difference between head and tails")
    pylab.xlabel("Number of flips")
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs)
    pylab.show()
    pylab.figure()
    pylab.title("Head/Tail Ratios")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("#Heads/#Tails")
    pylab.plot(xAxis, ratios)
    pylab.show()


def readInput():
    mini = int(raw_input('Enter min val: '))
    maxi = int(raw_input('Eter max val: '))
    return (mini, maxi)


def main():
    params = readInput()
    flipPlot(params[0], params[1])

if __name__ == '__main__':
    main()
