#зачем делать OwnError если по факту нужен встроенный ValueError?
class OwnError(Exception):
    def __init__(self):
        print("Нужно ввести число")

my_list = []
a = True
while a:
 inp_number = input("Введите число для списка: ")
 if inp_number == "stop":
     a = False
 try:
    inp_number = int(inp_number)
    my_list.append(inp_number)
 except ValueError:
    OwnError()
    pass
 print(my_list)



