def divis(arg_1, arg_2):
   if arg_2 == 0:
       return 'На ноль делить нельзя'
   else:
       return arg_1 / arg_2

print('Введите два числа')
a = int(input())
b = int(input())

print(divis(a,b))
