import pylab


def getData(filename):
    f = open(filename, 'r')
    distances = []
    masses = []
    f.readline()
    for line in f:
        d, m = line.split(",")
        distances.append(float(d.strip()))
        masses.append(float(m.strip()))
    f.close()
    return (masses, distances)


def plotData(inputFile):
    masses, distances = getData(inputFile)
    masses = pylab.array(masses)
    distances = pylab.array(distances)
    forces = masses * 9.81

    pylab.plot(forces, distances, 'bo', label="Measured Displacements")
    pylab.title("Measured displacement of Spring")
    pylab.xlabel("|Force| (Newtons)")
    pylab.ylabel("Distance (meters)")
    pylab.show()


def main():
    filename = "hookExp.csv"
    plotData(filename)

if __name__ == '__main__':
    main()
