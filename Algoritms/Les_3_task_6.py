#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

old_list = [random.randint(0, 100) for _ in range(10)]
print(f'Список случайных чисел {old_list}')
new_list = []
max_item = 0
max_item_i = 0
min_item = 100
min_item_i = 0
for i, item in enumerate(old_list):
    if item > max_item:
        max_item = item
        max_item_i = i
    if item < min_item:
        min_item = item
        min_item_i = i
if max_item_i > min_item_i:
    new_list = old_list[min_item_i + 1: max_item_i]
else:
    new_list = old_list[max_item_i + 1: min_item_i]
print(f'Минимальной значение массива - {min_item}, его место в массиве {min_item_i + 1}')
print(f'Максимальное значение массива - {max_item}, его место в массиве {max_item_i + 1}')
print(f'Сумма между максимальным и минимальным элементом {sum(new_list)}')