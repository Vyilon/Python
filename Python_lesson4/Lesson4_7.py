from math import factorial


def fact(n):
    for el in range(1, n):
        yield factorial(el)


for el in fact(7):
    print(el)
