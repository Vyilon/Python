#9.Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

max_n = 0
sum_max = 0

while True:
    n = int(input("Введите числа по одному, окончание ввода: 0 "))
    if n == 0:
        break
    sum_num = 0
    a = n
    while a != 0:
        sum_num = sum_num + a % 10
        a = a // 10
    if sum_num > sum_max:
        sum_max = sum_num
        max_n = n


print(f'Наибольшее по сумме чисел {max_n}, сумма его чисел {sum_max}')