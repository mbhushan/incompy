class Field(object):

    def __init__(self):
        self.drunks = {}

    def addDrunks(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Duplicate Drunk")
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in the field")
        xdist, ydist = drunk.takeStep()
        currentLocation = self.drunks[drunk]

        # lets use move methon of Location class to get new direction
        self.drunks[drunk] = currentLocation.move(xdist, ydist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in the field")
        return self.drunks[drunk]
