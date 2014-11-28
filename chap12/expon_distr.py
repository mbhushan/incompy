import pylab


def clear(n, p, steps):
    """Assumes n & steps to be positive ints and p to be a float"""
    numRemaining = [n]
    for s in range(steps):
        numRemaining.append(n*((1-p)**s))

    pylab.plot(numRemaining)
    pylab.xlabel("Time")
    pylab.ylabel("Molecules Remaining")
    pylab.title("Clearance of Drug")
    pylab.show()


def readInput():
    n = int(raw_input("Initial number of molecules: "))
    p = float(raw_input("probability of molecules being cleared: "))
    steps = int(raw_input("length of simulation: "))

    return (n, p, steps)


def main():
    n, p, steps = readInput()
    clear(n, p, steps)


if __name__ == '__main__':
    main()
