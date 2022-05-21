class Car:
    def __init__(self, speed, color, name, is_police):
     self.speed = speed
     self.color = color
     self.name = name
     self.is_police = bool(is_police)

    def go(self):
        print(f"Авто поехало")
    def stop(self):
        print(f"Авто остановилось")
    def turn(self, direction):
        self.direction = direction
        print(f"Авто поехало на {self.direction}")
    def show_speed(self):
        print(f"скорость авто {self.speed}")

class TownCar(Car):
    def show_speed(self):
        print(f"скорость авто {self.speed}")
        if (int(self.speed)) > 60:
            print("Превышение скорости для городского автомобиля")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f"скорость авто {self.speed}")
        if (int(self.speed)) > 40:
            print("Превышение скорости для рабочего автомобиля")

class PoliceCar(Car):
    pass

a = TownCar(65, "Blue", "Lada", True)
a.go()
a.stop()
a.turn("лево")
a.show_speed()
print(a.name)
print(a.color)
print(a.speed)
print(a.is_police)