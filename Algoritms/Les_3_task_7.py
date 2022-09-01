#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

my_list = [23, 34, 43, 68, 6, 342, 94, 34543, 56, 242]
print(f'Список исходный {my_list}')
min_item_1 = max(my_list) + 1
min_item_1_i = 0
for i, item in enumerate(my_list):
    if item < min_item_1:
        min_item_1 = item          #код полная дичь но работает
        min_item_1_i = i
min_item_2 = max(my_list) + 1
min_item_2_i = 0
my_list[min_item_1_i] = max(my_list) + 1
for i, item in enumerate(my_list):
    if min_item_2 > item:
        min_item_2 = item
        min_item_2_i = i

print(f'Первый минимальный элемент имеет значение = {min_item_1} его место в массиве {min_item_1_i+ 1}')
print(f'Второй минимальный элемент имеет значение = {min_item_2} его место в массиве {min_item_2_i+ 1}')
