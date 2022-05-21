class Stationery:
      title = "Канцелярские принадлжености"
      def draw(self):
          print(f"Запуск отрисовки ")

class Pen(Stationery):
      def __init__(self):
          self.title = "Ручка"
      def draw(self):
          print(f"Запуск отрисовки ручкой")

class Pencil(Stationery):
    def __init__(self):
        self.title = "Карандаш"
    def draw(self):
        print(f"Запуск отрисовки карандашом")

class Handle(Stationery):
    def __init__(self):
        self.title = "Маркер"
    def draw(self):
        print(f"Запуск отрисовки маркером")


a = Pencil()
print(a.title)
a.draw()
