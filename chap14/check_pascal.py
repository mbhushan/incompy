import random


def rollDice():
    return random.choice([1, 2, 3, 4, 5, 6])


def checkPascal(trials, rolls):
    ''' assuming trials is integer > 0, print estimate of winning. '''
    wins = 0.0
    for i in range(trials):
        for j in range(rolls):
            d1 = rollDice()
            d2 = rollDice()
            n = d1 + d2
            if n == 12:
                wins += 1
                break
    return wins/trials


def readInput():
    rolls = int(raw_input("enter number of rolls: "))
    trials = int(raw_input("enter number of trials: "))
    return rolls, trials


def main():
    r, t = readInput()
    ans = checkPascal(t, r)
    print "probability of double six with pair of dice: {}".format(ans)

if __name__ == '__main__':
    main()
