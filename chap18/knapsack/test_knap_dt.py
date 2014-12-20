from knap_decisiontree import maxVal
from Item import Item
import random


def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i), random.randint(1, maxVal),
                          random.randint(1, maxWeight)))
    return items


def bigTest(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = maxVal(items, 40)
    print "Items taken, "
    for item in taken:
        print item
    print "Total value of items taken: ", val


def main():
    nitems = int(raw_input("Enter num items: "))
    bigTest(nitems)

if __name__ == '__main__':
    main()
