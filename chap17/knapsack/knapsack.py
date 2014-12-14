from Item import Item


def value(item):
    return item.getItemValue()


def weightInverse(item):
    return 1.0/item.getItemWeight()


def density(item):
    return item.getItemValue()/item.getItemWeight()


def buildItems():
    names = ["clock", "painting", "radio", "vase", "book", "computer"]
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items


def greedy(items, maxWeight, keyFunction):
    """Assumes Items a list, maxWeight >= 0,
    keyFunction maps elements of Items to floats"""
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
        if totalWeight + itemsCopy[i].getItemWeight() <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getItemWeight()
            totalValue += itemsCopy[i].getItemValue()
    return (result, totalValue)


def evalGreedy(items, constraint, keyfunction):
    taken, val = greedy(items, constraint, keyfunction)
    print "Total value of taken items: ", val
    for i in taken:
        print '\t' + str(i)


def testGreedy(maxWeight=20):
    items = buildItems()
    print "Use greedy by value to fill knapsack of size:  ", maxWeight
    evalGreedy(items, maxWeight, value)

    print "\nUse greedy by weight to fill knapsack of size:  ", maxWeight
    evalGreedy(items, maxWeight, weightInverse)

    print "\nUse greedy by density to fill knapsack of size:  ", maxWeight
    evalGreedy(items, maxWeight, density)


def readInput():
    weight = float(raw_input("Enter max weight for knapsack: "))
    return weight


def main():
    weight = readInput()
    testGreedy(weight)


if __name__ == '__main__':
    main()
