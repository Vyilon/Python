def int_func(str):
    return str.title()

def int_func2(str):
    str = str.split()
    str2 = [int_func(i) for i in str]
    return (' '.join(str2))



print(int_func2('apple луна самолёт кукуруза ракета'))