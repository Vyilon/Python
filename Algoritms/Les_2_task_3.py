#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#Например, если введено число 3486, надо вывести 6843.

def numbers2(num):
    num = str(num)
    new_num = ''
    for i in range((len(num))):
        new_num += num[(len(num)-1) - i]
    return new_num


print(numbers2(34868989))