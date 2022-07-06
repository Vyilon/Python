from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    def __add__(self, other):
         return f'Сумма затраченной ткани равна: {(self.param / 6.5 + 0.5) + (2 * other.param + 0.3) :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Абстрактный метод одежда'


class Coat(Clothes):
    @property
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Абстрактный метод пальто'


class Costume(Clothes):
    @property
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        return 'Абстрактный метод костюм'


coat = Coat(50)
costume = Costume(100)
print(coat.consumption)
print(costume.consumption)
print(coat.abstract())
print(costume.abstract())
print(coat + costume)
