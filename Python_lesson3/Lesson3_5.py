summ = 0
a = True
while a:
    print('Вводите строку чисел разделенных пробелом (можно добавлять) , выход #')
    str = input()
    str = str.split()
    for i in str:
        if i == '#':
            a = False
        else:
            summ += int(i)
    print(summ)
