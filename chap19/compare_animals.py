from animal import Animal
import pylab


def compareAnimals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 0
    Builds a table of Euclidean distance between each animal"""
    colLables = []
    for a in animals:
        colLables.append(a.getName())

    rowLabels = colLables[:]
    tableVals = []
    # get distance between each pair of animals
    for a1 in animals:
        row = []
        for a2 in animals:
            if a1 == a2:
                row.append("--")
            else:
                dist = a1.distance(a2)
                row.append(round(dist, precision))
        tableVals.append(row)
    # produce the table
    table = pylab.table(rowLabels=rowLabels,
                        colLabels=colLables,
                        cellText=tableVals,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.2] * len(animals))
    table.scale(1, 2.5)
    pylab.axis('off')
    pylab.savefig('distances')
    pylab.show()


def main():
    rattlesnake = Animal('rattlesnake', [1, 1, 1, 1, 0])
    boa = Animal('boa\nconstrictor', [0, 1, 0, 1, 0])
    dartFrog = Animal('dart frog', [1, 0, 1, 0, 4])
    alligator = Animal('alligator', [1, 1, 0, 1, 4])
    animals = [rattlesnake, boa, dartFrog, alligator]
    compareAnimals(animals, 3)


if __name__ == '__main__':
    main()
