import random


def anyProb(trials):
    ''' Probability of 48 anorexics being born in some month'''
    anymonth48 = 0
    for t in range(trials):
        months = [0]*12
        for i in range(446):
            months[random.randint(0, 11)] += 1
        if max(months) >= 48:
            anymonth48 += 1
    aprob = anymonth48/float(trials)
    print "probability of atleast 48 births in same month: ", aprob


def main():
    anyProb(10000)


if __name__ == '__main__':
    main()
