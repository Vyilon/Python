print("Введите время в секундах")
t = int(input())
hours = t // 3600
min = (t % (hours*3600)) // 60
sec = t % ((hours*3600) + (min * 60))
print(hours, ":", min, ":", sec)

