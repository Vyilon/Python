import re
with open("6.txt", "r") as f_obj:
    my_dict ={}
    for line in f_obj:
        text = re.split('[ ()]', line)  #нагуглил такую конструкцию через просто сплит не получается отделить чифры от скобок
        sum = 0
        for i in range(len(text)):
            try:
                text[i] = int(text[i])  # пробуем преобразовать в int
            except:
                pass
            if isinstance(text[i], int):    #если int то складываем
                sum += text[i]
        my_dict[text[0]] = sum
    print(my_dict)