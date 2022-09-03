#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и
# ниже среднего.
from collections import namedtuple

company = namedtuple('company', ['name', 'q1', 'q2', 'q3', 'q4', 'y'])
companys = []
q = int(input("Введите количество предприятий: "))
total = 0
for i in range(q):
    name = input(f"Название {i + 1}-ого предприятия: ")
    q1 = int(input("Введите прибыль за 1 квартал: "))
    q2 = int(input("Введите прибыль за 2 квартал: "))
    q3 = int(input("Введите прибыль за 3 квартал: "))
    q4 = int(input("Введите прибыль за 4 квартал: "))
    y = q1 + q2 + q3 + q4
    total += y
    companys.append(company(name=name, q1=q1, q2=q2, q3=q3, q4=q4, y=y))
total_avg = total / q
print(f"Средняя прибыль за год для всех предприятий {round(total_avg, 2)}")
print(f'Предприятий, чья прибыль выше среднего: ')
for company in companys:
    if company.y > total_avg:
        print(company.name)
print(f'Предприятий, чья прибыль ниже среднего: ')
for company in companys:
    if company.y < total_avg:
        print(company.name)


