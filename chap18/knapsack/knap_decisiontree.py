from Item import Item


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total weight of a solution to the
    0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getItemWeight() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]

        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getItemWeight())
        withVal += nextItem.getItemValue()

        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        # choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem, ))
        else:
            result = (withoutVal, withoutToTake)

    return result


def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []

    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(Items, 5)
    for item in taken:
        print item
    print "Total value of taken item: ", val


def main():
    smallTest()


if __name__ == '__main__':
    main()
