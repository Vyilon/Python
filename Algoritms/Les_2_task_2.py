#2.Посчитать четные и нечетные цифры введенного натурального числа.
#Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def numbers(num):
     even = ""
     odd = ""
     even_count = 0
     odd_count = 0
     num = str(num)
     for i in range(len(num)):
         if int(num[i]) % 2 == 0:
             even += str(num[i]) + ' '
             even_count += 1
         else:
             odd += str(num[i]) + ' '
             odd_count +=1
     return f'Четные числа введенного числа {even} их количество {even_count}  Нечетные числа введенного числа {odd} их количество {odd_count}'

print(numbers(34560))
