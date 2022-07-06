from itertools import count
from itertools import cycle

def gen1(arg1):
    for el in count(arg1):
        if el > 10:
            print('\n')
            break
        else:
            print(el, end=" ")

def gen2(arg2, arg3):
    arg2 = ("".join(map(str, arg2)))
    с = 0
    for el in cycle(arg2):
        if с > int(arg3):
            break
        print(el, end=" ")
        с += 1

gen1(4)

gen2([1, 2, 4, 6], 14)
