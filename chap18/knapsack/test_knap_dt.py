from knap_decisiontree import maxVal
from Item import Item
import random


def fastMaxVal(toConsider, avail, memo={}):
    """Assumes toConsider a list of items, avail a weight
    memo used only by recursive calls
    Returns a tuple of the total weight of a solution to the
    0/1 knapsack problem and the items of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getItemWeight() > avail:
        # explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        # explore left branch
        withVal, withToTake = \
            fastMaxVal(toConsider[1:], avail - nextItem.getItemWeight(), memo)
        withVal += nextItem.getItemValue()

        # explore right branch
        withoutVal, withoutTaken = fastMaxVal(toConsider[1:], avail, memo)

        # choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutTaken)
    memo[(len(toConsider), avail)] = result
    return result


def buildManyItems(numItems, maxval, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i), random.randint(1, maxval),
                          random.randint(1, maxWeight)))
    return items


def bigTest(numItems):
    items = buildManyItems(numItems, 100, 100)
    # val, taken = maxVal(items, 40)
    val, taken = fastMaxVal(items, 1000)
    print "Items taken, "
    for item in taken:
        print item
    print "Total value of items taken: ", val


def main():
    nitems = int(raw_input("Enter num items: "))
    bigTest(nitems)

if __name__ == '__main__':
    main()
