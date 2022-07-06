with open("2.txt", "a+") as f_obj:
    while True:
     content = input('Введите текст: ')
     print(content, file=f_obj)
     if not content:
       break
    f_obj.seek(0)
    lines = 0
    for line in f_obj:
        lines +=1
        print(f"Строка {lines} , количество слов в строке {len(line.split())}")
