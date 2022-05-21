import time
class TrafficLight:
    __color = "Горит красный"
    def running(self):
     print(self.__color)      #почему то меняет приватный атриубут как защищенный
     time.sleep(7)
     self.__color = "Горит желтый"
     print(self.__color)
     time.sleep(2)
     self.__color = "Горит зеленый"
     print(self.__color)
     time.sleep(4)

a = TrafficLight()
a.running()