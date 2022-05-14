my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)
new_list = [x for i, x in enumerate(my_list) if my_list.count(x) < 2]
print(new_list)