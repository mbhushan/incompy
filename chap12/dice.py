import random


def rollDice():
    return random.choice([1, 2, 3, 4, 5, 6])


def main():
    n = rollDice()
    print 'dice: {}'.format(n)


if __name__ == '__main__':
    main()
