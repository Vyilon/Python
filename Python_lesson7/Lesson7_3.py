class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return f'Создана новая клетка, сумма ячеек {int(self.count + other.count)}'
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return f'Разность клеток {self.count - other.count}'
        else:
            return f'Вычитание невозможно'

    def __mul__(self, other):
        return f'Создана новая клетка, произведение ячеек {int(self.count * other.count)}'
        return  Cell(self.count * other.count)

    def __truediv__(self, other):
        return f'Создана новая клетка, результат деления ячеек {int(self.count // other.count)}'
        return Cell(int(self.count // other.count))

    def make_order(self, new_count):
        a = int(self.count)
        b = 0
        my_string = ""
        while a > 0:
            my_string += "*"
            b += 1
            if b == int(new_count):
                my_string += '\ n' # так и не понял как записать в виде \n чтобы не переносило строку
                b = 0
            a -= 1
        return my_string


a = Cell(25)
b = Cell(5)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(5))
