#Pandas
# Для некоторых заданий, возможно, придется обратиться к документации: https://pandas.pydata.org/docs/
#
# Скачайте любой табличный датасет (или создайте тестовый пример самостоятельно), например, с https://www.kaggle.com/datasets
#
# Загрузите данные и проанализируйте их (используя функции .info и .describe)
#
# Выведите отдельно интересующую вас колонку и столбец
#
# Numpy
# Для некоторых заданий, возможно, придется обратиться к документации: https://numpy.org
#
# Создайте вектор (одномерный массив) размера 10, заполненный нулями
# Создайте вектор размера 10, заполненный числом 5.8
# Создйте массив 3x3x3 со случайными значениями
# Создайте 8x8 матрицу и заполнить её в шахматном порядке
# Cоздайте матрицу 4 на 4 и заполните ее произвольными числами (понадобиться в дальйнешем)
# Scipy
# Возьмите интеграл ∫10−3sin(x)∗x2dx
# Найдите определитель, обратную матрицу и собственные значения к матрице из последнего пункта раздела Numpy
# Matplotlib/Seaborn
# Нарисуйте график sin(x), подпишите оси, добавьте сетку
# Нарисуйте график sin(x) и cos(x) на одном subplot'е и на разных, задайте цвета, которые вам больше нравятся
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy
import matplotlib
from numpy import sin
import matplotlib.pyplot as plt

#pandas
a = pd.read_csv("India_Menu.csv")
print(a.head(3))
print(a.info)
print(a.describe())
print(a['Sodium (mg)'])

#nympy
b = np.zeros(10)
print(b)

c = np.array(range(10), float)
c.fill(5.8)
print(c)

d = np.random.randint(0, 5, size=(3, 3))
print(d)

e = np.zeros((8, 8), dtype=int)
e[1::2, ::2] = 1
e[::2, 1::2] = 1
print(e)

f = np.random.randint(0, 10, size=(4, 4))
print(f)

#scipy

f1 = lambda x: sin(x)*x**2
print(scipy.integrate.quad(f1, -3, 10))

g = scipy.linalg.inv(f)  #обратная матрица
print(g)
h = scipy.linalg.det(f) #определитель
print(h)
i, j = scipy.linalg.eigh(f) #собственные значения к матрице
print("Selected eigenvalues :", i)
print("Complex ndarray :", j)

#Matplotlib
lag = 0.1
x = np.arange(0.0, 2*np.pi, lag)
y = np.sin(x)

fig = plt.Figure()
plt.plot(x, y)
plt.grid()
plt.ylabel('Ось Y')
plt.xlabel('Ось X')
plt.show()

x2 = np.arange(0.0, 2*np.pi, lag)
y2 = np.sin(x2)
x3 = np.arange(0.0, 2*np.pi, lag)
y3 = np.cos(x3)
fig2 = plt.Figure()
plt.plot(x2, y2, '-', x3, y3, '--')
plt.grid()
plt.show()

x4 = np.arange(0.0, 2*np.pi, lag)
y4 = np.sin(x4)
x5 = np.arange(0.0, 2*np.pi, lag)
y5 = np.cos(x5)
fig3 = plt.Figure(figsize=(12, 7))
plt.subplot(1, 2, 1)
plt.plot(x4, y4, '-')
plt.subplot(1, 2, 2)
plt.plot(x5, y5, '--')
plt.show()