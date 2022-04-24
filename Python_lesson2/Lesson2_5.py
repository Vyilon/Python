my_list = [7, 5, 3, 3, 2]
print('Напишите новый элемент')
text = int((input()))
max = max(my_list)
min = min(my_list)
if text > max:
    my_list.insert(0, text)
elif text < min:
    my_list.append(text)
else:
    a = my_list.index(text)
    my_list.insert(a, text)
print(my_list)