a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11]
print(a)
for i in range(0, (len(a)-1), 2):
   a[i+1], a[i] = a[i], a[i+1]
print(a)









