import datetime


class Person(object):

    def __init__(self, name):
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastname = name[lastBlank+1:]
        except:
            self.lastname = name
        self.birthday = None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastname

    def setBirthday(self, birthdate):
        self.birthday = birthdate

    def getAge(self):
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname

    def __str__(self):
        return self.name

me = Person("Mani Bhushan")
him = Person('Shreyansh Bhushan')
her = Person('Kumari Archana')

print me.getLastName()
print him.getLastName()
print her.getLastName()

me.setBirthday(datetime.date(1983, 11, 25))
him.setBirthday(datetime.date(2013, 1, 8))
her.setBirthday(datetime.date(1983, 12, 12))

print him.getName(), ' is ', him.getAge(), ' days old!'
