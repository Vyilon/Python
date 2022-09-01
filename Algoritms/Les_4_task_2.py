# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
import math
import cProfile

def eratosthenes(n):
    sieve = list(range((n * 3 * int(math.log(n)))))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    sieve = [i for i in sieve if i != 0]
    return sieve[n-1]



def classic(x):
    sieve = [x for x in range(2, x * 3 * int(math.log(x))) if not [n for n in range(2, x) if not x % n]]
    return sieve[x-1]

# cProfile.run('eratosthenes(10)')
# 23 function calls in 0.000 seconds
# cProfile.run('classic(10)')
# 6 function calls in 0.000 seconds
# cProfile.run('eratosthenes(50)')
# 93 function calls in 0.000 seconds
# cProfile.run('classic(50)')
# 6 function calls in 0.001 seconds


#  "Les_4_task_2.eratosthenes(10)"
# 1000 loops, best of 5: 18.3 usec per loop
# "Les_4_task_2.classic(10)"
# 1000 loops, best of 5: 141 usec per loop
#  "Les_4_task_2.eratosthenes(100)"
# 1000 loops, best of 5: 329 usec per loop
# "Les_4_task_2.classic(100)"
# 1000 loops, best of 5: 44.1 msec per loop  Считалось 4 минуты

#Вывод - классический алгоритм намного медленнее, но при этом имеет гораздо меньше вызовов функций  внутри себя!