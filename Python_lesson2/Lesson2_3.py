print('Введите номер месяца')
month = int(input())
list_months = ['зима', 'весна', 'лето', 'осень']
dict_months = {1 : 'зима' ,2 :'весна' ,3 :'лето', 4 : 'осень'}
if 3 <= month <= 5:
    print('Время года через список', list_months[1])
    print('Время года через словарь',dict_months.get(2))
elif 6 <= month <= 8:
    print('Время года через список', list_months[2])
    print('Время года через словарь', dict_months.get(3))
elif 9 <= month <= 11:
    print('Время года через список', list_months[3])
    print('Время года через словарь', dict_months.get(4))
else:
    print('Время года через список', list_months[0])
    print('Время года через словарь', dict_months.get(1))
