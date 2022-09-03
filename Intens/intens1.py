number = str(input('Введите значение \n'))
if number[0] == '-':
    number = number[1:]
number = number.replace('.', '', 1)
if number.isdigit():
    print('Correct')
else:
    print('Wrong')
