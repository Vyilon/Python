#По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.
x1 = int(input("Введите x координаты первой точки "))
y1 = int(input("Введите y координаты первой точки "))
x2 = int(input("Введите x координаты второй точки "))
y2 = int(input("Введите y координаты второй точки "))
k = (y1 - y2) / (x1 -x2)
b = y2 - k * x2
print(f'Полученное выражение равно  y = {round(k,2)}*x + {round(b,2)}')