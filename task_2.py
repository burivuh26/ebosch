from abc import abstractmethod


class Thing:
    result = 0

    def __init__(self, num):
        self.num = num

    @property
    @abstractmethod
    def spending(self):
        pass

    def __add__(self, other):
        Thing.result += self.spending + other.spending
        return Suit(0)

    def __str__(self):
        return f'{Thing.result}'


class Coat(Thing):
    @property
    def spending(self):
        return self.num / 6.5 + 0.5


class Suit(Thing):
    @property
    def spending(self):
        return self.num * 2 + 0.3


coat = Coat(56)
suit = Suit(180)
print(coat + suit)
