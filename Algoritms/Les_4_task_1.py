#1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

#На примере задачи 3 из второго урока.  Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#Например, если введено число 3486, надо вывести 6843.
import cProfile

def numbers1(num):
    num = str(num)
    new_num = ''
    for i in range((len(num))):
        new_num += num[(len(num)-1) - i]
    return new_num

def numbers2(num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num = num // 10
    return result

def numbers3(num):
    num = str(num)
    result = num[::-1]
    return result

#cProfile.run(numbers1(15896354865836))
#3 function calls in 0.000 seconds

#cProfile.run(numbers3(15896354865836))
#3 function calls in 0.000 seconds

#cProfile.run(numbers2(15896354865836))
#2 function calls in 0.000 seconds


#  "Les_4_task_1.numbers1(3486)"
# 1000 loops, best of 5: 1.57 usec per loop
# "Les_4_task_1.numbers2(3486)"
# 1000 loops, best of 5: 988 nsec per loop
# "Les_4_task_1.numbers3(3486)"
# 1000 loops, best of 5: 555 nsec per loop

# "Les_4_task_1.numbers1(15896354865836)"
# 1000 loops, best of 5: 3.6 usec per loop
# "Les_4_task_1.numbers2(15896354865836)"
# 1000 loops, best of 5: 3.95 usec per loop
# "Les_4_task_1.numbers3(15896354865836)"
# 1000 loops, best of 5: 612 nsec per loop

# "Les_4_task_1.numbers1(1589635486583664576073457017354076405742)"
# 1000 loops, best of 5: 8.99 usec per loop
# "import Les_4_task_1" "Les_4_task_1.numbers2(1589635486583664576073457017354076405742)"
# 1000 loops, best of 5: 12.7 usec per loop
# "Les_4_task_1.numbers3(1589635486583664576073457017354076405742)"
# 1000 loops, best of 5: 804 nsec per loop

#Самый лучший вариант -  номер 3 с представлением в виде списка. Он имеет минимальные сроки выполнения при любых входящих
#значениях. Вариант 2  при небольших значениях эффекивнее варианта 1, но при увеличении длины вводимого числа начинает
#ему уступать. Вариант 2 и вариант 1 уступают в производительности варианту 3 очень сильно




