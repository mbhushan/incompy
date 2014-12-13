import pylab


def plotHousing(impression):
    """Assumes impression a str. Must be one of 'flat',
    'volatile,' and 'fair' Produce bar chart of housing prices over time"""
    f = open("midWestHousingPrices.txt", 'r')
    # Each line of file contains year quarter price
    labels, prices = ([], [])
    for line in f:
        year, qtr, price = line.split()
        label = year[2:4] + "\n Q" + qtr[1]
        labels.append(label)
        prices.append(float(price)/1000)
    quarters = pylab.arange(len(labels))
    width = 0.8
    # if impression == 'flat':
    #    pylab.semilogy()
    pylab.bar(quarters, prices, width)
    pylab.xticks(quarters+width/2.0, labels)
    pylab.title("Housing prices in US Midwest")
    pylab.xlabel("Quarter")
    pylab.ylabel("Average price ($1000\'s)")
    if impression == 'flat':
        pylab.semilogy()
        pylab.ylim(10, 10**3)
    elif impression == 'volatile':
        pylab.ylim(180, 220)
    elif impression == 'fair':
        pylab.ylim(150, 250)
    else:
        raise ValueError
    pylab.show()


def readInput():
    val = 0
    try:
        val = int(raw_input("flat, volatile or fair <1, 2, or 3> ? "))
    except ValueError:
        print "Bad input, try again!!"
        readInput()
    if val not in [1, 2, 3]:
        print "Bad Choice, try again!!"
    else:
        return val


def main():
    val = readInput()
    if val == 1:
        plotHousing('flat')
    elif val == 2:
        plotHousing('volatile')
    else:
        plotHousing('fair')


if __name__ == '__main__':
    main()
