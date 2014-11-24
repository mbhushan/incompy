import merge_sort
import string


def lastFirstName(name1, name2):
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')
    if name1[1] != name2[1]:
        return name1[1] < name2[1]
    else:
        name1[0] < name2[0]


def firstLastName(name1, name2):
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')
    if name1[0] != name2[0]:
        return name1[0] < name2[0]
    else:
        name1[1] < name2[1]


def readInput():
    n = int(raw_input('How many names: '))
    print 'Enter names below: '
    names = []
    while n > 0:
        ip = raw_input()
        names.append(ip)
        n -= 1
    return names


def main():
    L = readInput()

    while True:
        s = raw_input('sort by firstname or lastname, enter <f/l>: ')
        if s == 'f' or s == 'l':
            break
        else:
            print 'wrong option - please try again!'
    if s == 'f':
        sl = merge_sort.mergeSort(L, firstLastName)
        print 'list sorted on first name: '
        print sl
    else:
        sl = merge_sort.mergeSort(L, lastFirstName)
        print 'list sorted on second name: '
        print sl


if __name__ == '__main__':
    main()
