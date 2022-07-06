class Date:
    date = 0
    month = 0
    year = 0
    my_date = ""

    def __init__(self, my_date):
        Date.my_date = my_date

    @staticmethod
    def my_static():
        if Date.date > 31 or Date.date < 1:
            print("Ошибка в вводе даты")
        elif Date.month > 12 or Date.month < 1:
            print("Ошибка в вводе месяца")
        elif Date.year > 2022:
            print("Ошибка в вводе года")
        else:
            print("Формат введенной даты верен")

    @classmethod
    def my_classmethod(cls):
        datex = cls.my_date
        datex = datex.split("-")
        Date.date = int(datex[0])
        Date.month = int(datex[1])
        Date.year = int(datex[2])
        print(f"Дата {Date.date}, месяц {Date.month}, год {Date.year}")


a = Date("12-5-2000")
Date.my_classmethod()
a.my_static()