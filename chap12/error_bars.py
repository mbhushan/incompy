import coinflip_norm_distr
import pylab


def showErrorBars(mini, maxi, trials):
    means, sds = [], []
    xVals = []
    for e in range(mini, maxi+1):
        xVals.append(2**e)
        headFrac, mean, sd = coinflip_norm_distr.flipSim(2**e, trials)
        means.append(mean)
        sds.append(sd)

    pylab.errorbar(xVals, means, yerr=2*pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean fraction of Heads! (' + str(trials) + ' trials)')
    pylab.xlabel('Number of flips per trial.')
    pylab.ylabel('Fraction of heads & 95% confidence')
    pylab.show()


def readInput():
    mini = int(raw_input('Enter min value: '))
    maxi = int(raw_input('Enter max value: '))
    trials = int(raw_input('Enter number of trials: '))
    return (mini, maxi, trials)


def main():
    mini, maxi, trials = readInput()
    showErrorBars(mini, maxi, trials)


if __name__ == '__main__':
    main()
