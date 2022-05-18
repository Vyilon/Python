with open("5.txt", "w") as f_obj:
    print(input('Введите числа через пробел '), end="", file=f_obj)

with open("5.txt", "r") as new_obj:
    for line in new_obj:
        text = line.split(' ')
        text_int = list(map(int, text))
    print(f'Сумма числе в строке {sum(text_int)}')
