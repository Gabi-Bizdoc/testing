import random


class Sobolan(object):

    mustati = 6

    def __init__(self, name='Gigi'):
        super(Sobolan, self).__init__()
        self._name = name

    def chitz_chitz(self):
        print("Chitz chitz! Unde-mi branzu' lu' %s?" % self._name)

    def __mul__(self, tata):
        new_name = "%s%s" % (
            self._name[:len(self._name) // 2],
            tata._name[len(tata._name) // 2:])

        return Sobolan(new_name)

    def __eq__(self, altu):
        return self._name == altu._name

    def produ_numere_random(self):
        """Return random numbers between 0 and 10."""
        return random.randint(0, 10) - 1

    @classmethod
    def fabrica_new_sobolan(cls):
        return cls(str(random.randint(0, 100)))


class SobolanNextLevel(Sobolan):

    def chitz_chitz(self):
        super(SobolanNextLevel, self).chitz_chitz()
        print("Chitz chitz! Te tau, daca nu-mi dai branzu'!")

    def produ_numere_random(self):
        # the child should always be able to behave as his parent.
        return random.randint(4, 5)
