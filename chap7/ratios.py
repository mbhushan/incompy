
def getRatios(vect1, vect2):
    ''' Assumes: vect1 & vect2 are list of numbers of equal length
    Returns: a list of meaningful values vect1[i]/vect2[i] '''
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan'))  # nan = Not a Number
        except:
            raise ValueError('getRatios called with Bad Arguments!')
    return ratios


def inputVect():
    st = raw_input('Enter comma separated numbers: ')
    st = st.split(",")

    nums = [int(n) for n in st]
    return nums

vect1 = inputVect()
vect2 = inputVect()

ratios = getRatios(vect1, vect2)

print 'The ratios are: '
for r in ratios:
    print r
