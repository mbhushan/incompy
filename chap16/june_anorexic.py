import random


def juneProb(trials):
    ''' Probability of 48 anorexics being born in June '''
    june48 = 0
    for trial in range(trials):
        june = 0
        for i in range(446):
            if random.randint(1, 12) == 6:
                june += 1
        if june >= 48:
            june48 += 1
    jprob = june48/float(trials)
    print 'Probability of at least 48 births in june: ', jprob


def main():
    juneProb(10000)

if __name__ == '__main__':
    main()
