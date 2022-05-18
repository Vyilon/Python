with open("4.txt", "r") as f_obj:
    i = 0
    rus_list = ['Один', 'Два', 'Три', 'Четыре']
    for line in f_obj:
        text = line.split()
        text[0] = rus_list[i]
        i += 1
        with open('4new.txt', 'a') as new_obj:
            print(' '.join(text), file=new_obj)



