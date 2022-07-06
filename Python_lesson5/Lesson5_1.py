with open("python.txt", "w") as f_obj:
    while True:
     content = input('Введите текст: ')
     print(content, file=f_obj)
     if not content:
       break
