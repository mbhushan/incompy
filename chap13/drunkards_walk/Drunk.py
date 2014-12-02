import random


class Drunk(object):

    def __init__(self, name=None):
        """ Assumes name is str """
        self.name = name

    def __str__(self):
        if self:
            return self.name
        else:
            return 'Anonymous'


class UsualDrunk(Drunk):

    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class ColdDrunk(Drunk):

    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class EWDrunk(Drunk):

    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
