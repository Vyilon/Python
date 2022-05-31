class Complex_number:
    def __init__(self, txt):
        self.txt = txt
        if not isinstance(txt, complex):
          print("Введено не комплексное число")

    def __add__(self, other):
        return Complex_number(self.txt + other.txt)

    def __mul__(self, other):
        return Complex_number(self.txt * other.txt)

    def __str__(self):
       return f"Результат вычисления {self.txt}"

a = Complex_number(2 + 4j)
b = Complex_number(47 + 5j)
print(a+b)
print(a*b)

