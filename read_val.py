
def readVal(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg + ' ')
        try:
            val = valType(val)
            return val
        except ValueError:
            print val, errorMsg

val = readVal(int, "Enter integer: ", "is not an integer")

print "checking readVal function: ", val
