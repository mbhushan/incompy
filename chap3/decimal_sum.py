# sum of decimal numbers entered by user.

iput = raw_input("Enter comma separated decimal numbers: ")

iput = iput.strip()
iput = iput.split(",")

dsum = 0.0
for n in iput:
    n = float(n)
    dsum +=n

print "Total sum of input decimal numbers: {}".format(dsum)
