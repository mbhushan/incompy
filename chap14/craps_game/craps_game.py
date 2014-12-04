import random


class CrapsGame(object):

    def __init__(self):
        self.passwins, self.passlosses = (0, 0)
        self.dpwins, self.dplosses, self.dppushes = (0, 0, 0)

    def rollDie(self):
        return random.choice([1, 2, 3, 4, 5, 6])

    def playhandFast(self):
        # An alternative, faster, implementation of playHand
        pointsDict = {4: 1/3.0, 5: 2/5.0, 6: 5/11.0, 8: 5/11.0,
                      9: 2/5.0, 10: 1/3.0}
        throw = self.rollDie() + self.rollDie()
        if throw == 7 or throw == 11:
            self.passwins += 1
            self.dplosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passlosses += 1
            if throw == 12:
                self.dppushes += 1
            else:
                self.dpwins += 1
        else:
            if random.random() < pointsDict[throw]:
                self.passwins += 1
                self.dplosses += 1
            else:
                self.passlosses += 1
                self.dpwins += 1

    def playHand(self):
        throw = self.rollDie() + self.rollDie()
        if throw == 7 or throw == 11:
            self.passwins += 1
            self.dplosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passlosses += 1
            if throw == 12:
                self.dppushes += 1
            else:
                self.dpwins += 1
        else:
            point = throw
            while True:
                throw = self.rollDie() + self.rollDie()
                if throw == point:
                    self.passwins += 1
                    self.dplosses += 1
                    break
                elif throw == 7:
                    self.passlosses += 1
                    self.dpwins += 1
                    break

    def passResult(self):
        return (self.passwins, self.passlosses)

    def dpResults(self):
        return (self.dpwins, self.dplosses, self.dppushes)
