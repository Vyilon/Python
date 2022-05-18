with open("3.txt", "r") as f_obj:
    poor = []
    salary = []
    for line in f_obj:
        text = line.split()
        salary.append(int(text[1]))
        if int(text[1]) < 20000:
            poor.append(text[0])
    sal_sum = sum(salary)
    print(f"Сотрудники получающие меньше 20000 это {' '.join(poor)} ")
    print(f"Средняя зарплата {sal_sum/len(salary)} ")