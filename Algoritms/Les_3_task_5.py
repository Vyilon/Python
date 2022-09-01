#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

new_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Список случайных чисел {new_list}')
max_item = -100
max_item_i = 0
for i, item in enumerate(new_list):
    if 0 > item > max_item:
        max_item = item
        max_item_i = i
print(f'Максимальное отрицательное значение массива  {max_item}, его место в массиве {max_item_i + 1}')