#Пользователь вводит две буквы. Определить их порядковый
#номер в алфавите и рассчитать число букв между ними.
a = ord(input('Введите первую букву '))
b = ord(input('Введите вторую букву '))
print(f'Порядковый номер первой буквы {a  -ord("a")+ 1}')
print(f'Порядковый номер второй буквы {b - ord("a")+ 1}')
print(f'Число букв между ними {abs(a - b) - 1}')
