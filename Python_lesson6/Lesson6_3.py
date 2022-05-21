class Worker:
    def __init__(self, name, surname, position, wage, bonus):
     self.name = name
     self.surname = surname
     self.position = position
     self._income = {"оклад": wage, "бонус": bonus}

class Position(Worker):
     def get_full_name(self):
        print(f"{self.name} {self.surname}")

     def get_total_income(self):
        my_dict = self._income
        salary = int(my_dict["оклад"]) + int(my_dict["бонус"])
        print(f"Доход с учетом премии {salary}")

a = Position("Иван","Сидоров", "Старший помошник", 50000, 20000)
a.get_full_name()
a.get_total_income()
