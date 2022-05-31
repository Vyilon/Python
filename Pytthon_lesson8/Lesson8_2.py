class OwnError(Exception):
   def __init__(self, txt):
    self.txt = txt

inp_number = input("Введите делимое число: ")
inp_div = input("Введите делитель: ")

try:
    inp_number = int(inp_number)
    inp_div = int(inp_div)
    if inp_div == 0:
      raise OwnError("На ноль делить нельзя")
except ValueError:
     print("Вы ввели не число")
except OwnError as err:
      print(err)
else:
      print(f"Все хорошо. Результат деления: {inp_number/inp_div}")