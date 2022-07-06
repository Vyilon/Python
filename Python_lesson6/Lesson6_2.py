class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def road_mass(self, asphault_mass, thickness):
        self.asphault_mass = asphault_mass
        self.thickness = thickness
        mass = self._lenght * self._width * self.asphault_mass * self.thickness
        print(f"Масса афальта для дороги равна {int(mass/1000)} тонн")

a = Road(5000, 20)
a.road_mass(25, 5)
