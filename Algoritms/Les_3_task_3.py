# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

new_list = [random.randint(0, 100) for _ in range(10)]
print(f'Список случайных чисел {new_list}')
max_item = 0
max_item_i = 0
min_item = max(new_list) + 1
min_item_i = 0
for i, item in enumerate(new_list):
    if item > max_item:
        max_item = item
        max_item_i = i
    if item < min_item:
        min_item = item
        min_item_i = i
    new_list[max_item_i] = min_item
    new_list[min_item_i] = max_item

print(f'Минимальной значение массива - {min_item}, его место в массиве {min_item_i + 1}')
print(f'Максимальное значение массива - {max_item}, его место в массиве {max_item_i + 1}')
print(f'Список в котором поменены значения местами  {new_list}')




