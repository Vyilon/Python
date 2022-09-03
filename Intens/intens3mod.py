import re

def read_file(file):
    with open(file, 'r', encoding='UTF=8') as f:
        my_str = f.read()
        my_str = re.sub('[)|(|.|,|:|!]', '', my_str)
        my_str = my_str.lower()
        my_list = my_str.split(' ')
        return my_list

def save_file(file, str):
    my_set = set(str)
    my_new_list = list(my_set)
    my_new_list.sort()
    with open(file, 'w', encoding='UTF=8') as f:
        f.write(f'Количество уникальных слов = {len(my_new_list)} \n')
        for item in my_new_list:
            f.write(item)
            f.write('\n')

