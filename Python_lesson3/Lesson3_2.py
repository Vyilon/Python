print('Введите имя')
name = input()
print('Введите  фамилию')
family = input()
print('Введите год рождения')
birth = input()
print('Введите город проживания')
place = input()
print('Введите e-mail')
e_mail = input()
print('Введите телефон')
tel = input()

def my_func(**dates):
    return dates

print((my_func(Name = name, Family = family, Birthday = birth, Place = place, E_mail = e_mail, Telephone = tel)))
