my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
new_list = [x for i, x in enumerate(my_list) if my_list[i] > my_list[i-1]]
# Не знаю как убрать первое сравнение чтобы первым было число 12 а не 300, как не пробовал всегда out o range
print(new_list)