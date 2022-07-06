import json
with open("7.txt", "r") as f_obj:
    dict_profit ={}  #пустой словарь с прибылью
    average = [] #пустой список для расчета средней прибыли
    my_list = []
    for line in f_obj:
        data = line.split(' ')
        income = int(data[2]) - int(data[3])  #расчет прибыли
        if income > 0:
            dict_profit[data[0]] = income
            average.append(income)         #добавляем к среднее прибыли только если прибыль положительная
        else:
            dict_profit[data[0]] = income
    average_value = (sum(average))/len(average)
    average_profit = {'Average_profit': average_value}
    my_list.append(dict_profit)
    my_list.append(average_profit)
    print(my_list)
with open("7json.json", "w") as write_f:
    json.dump(my_list, write_f)
