print('Введите выручку')
a = int(input())
print('Введите издержки')
b = int(input())
if a > b :
    print('У вас прибыль, рентабельность выручки =', a / b)
    print('Введите число сотрудников')
    peoples = int(input())
    print('Прибыль на одного сотрудника =' , (a-b)/peoples)
else :
    print('У вас убыток')