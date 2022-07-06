from sys import argv

script_name, num1, num2, num3 = argv

def calc(a,b,c):
    print(f'Заработная плата = {a*b + c}')

calc(int(num1), int(num2), int(num3))


# if __name__ == '__main__':       #работает без этого
#     help()