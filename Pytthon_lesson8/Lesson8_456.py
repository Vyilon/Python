class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    my_dict = {"Printer": 0, "Scanner": 0, "Xerox": 0} #словарь остатков на складе

class Equipment:
    def __init__(self, weigth, price, color):
        self.weigth = weigth
        self.price = price
        self.color = color

    @classmethod
    def get_classname(cls):   #функция возврата имени класса объекта
        return cls.__name__

    def to_warehouse(self, quantity):  #функция отправки на склад с проверкой значения
        self.quantity = quantity
        if Equipment.check(quantity) == 1:
            Warehouse.my_dict[self.get_classname()] += quantity
            print(Warehouse.my_dict)

    def to_company(self, quantity):    #функция отправки в компанию с проверкой значения
        self.quantity = quantity
        if Equipment.check(quantity) == 1:
            Warehouse.my_dict[self.get_classname()] -= quantity
            print(Warehouse.my_dict)

    def check(txt): #проверка правильности введения числа
        try:
            txt = int(txt)
            if txt < 0:
                raise OwnError("Вы ввели отрицательное число!")
        except ValueError:
            print("Вы ввели не число")
        except OwnError as err:
            print(err)
        else:
            return 1

class Printer(Equipment):
    def __init__(self, weigth, price, color, speed):
        super().__init__(weigth, price, color)
        self.speed = speed

class Scanner(Equipment):
    def __init__(self, weigth, price, color, light):
        super().__init__(weigth, price, color)
        self.light = light

class Xerox(Equipment):
    def __init__(self, weigth, price, color, voltage):
        super().__init__(weigth, price, color)
        self.voltage = voltage

hp = Printer(34, 54, "black", 34)
hp.to_warehouse(5)
hp.to_company(3)
lg = Scanner(34, 54, "white", 54)
lg.to_warehouse(5)
lg.to_company(3)
wd = Xerox(34, 54, "Blue", 220)
wd.to_warehouse(15)
wd.to_company(4)


