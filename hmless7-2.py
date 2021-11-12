from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, v):
        self.v = v

    @property
    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        Clothes.result += self.expense + other.expense
        return Costume(0)

    def __str__(self):
        result_new = Clothes.result
        Clothes.result = 0
        return f'{result_new}'


class Coat(Clothes):
    @property
    def expense(self):
        return round(self.v / 6.5) + 0.5


class Costume(Clothes):
    @property
    def expense(self):
        return round((2 * self.v + 0.3) / 100)


coat = Coat(55)
costume = Costume(190)
print(coat + costume + coat)
