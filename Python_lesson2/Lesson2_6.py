print('Напишите сколько будет товаров')
number = int((input()))
my_list = []
for i in range(number):
    print('Введите в товаре ', i+1, ' название')
    name = input()
    print('Введите в товаре ', i + 1, ' цену')
    price = input()
    print('Введите в товаре ', i + 1, ' количество')
    quan = input()
    print('Введите в товаре ', i + 1, ' единицу измерения')
    unit = input()
    my_dict= {'название' : name, 'цена' : price, 'количество' : quan, 'единица измерения' : unit}
    my_list.insert(i+1,(i+1, my_dict))
    my_tuple = tuple(my_list)
print(my_tuple)
dict2 = dict[my_tuple]




