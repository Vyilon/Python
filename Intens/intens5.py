# Разработайте класс Logger, который:
# 1. Создаёт файл лога при инициализации объекта (по указанному пути или по умолчанию в корневой
# папке).
# *Обеспечить существование только одного объекта этого класса (паттерн Singleton)
# 2. Название файла должно иметь формат log_dd.mm.yy.
# 3. Внутри должен быть приватный метод, который возвращает текущую дату.
# 4. Все события одного дня должны писаться в один файл. Если день меняется, должен создаваться новый
# файл при записи в лог по шаблону из п.2
# 5. Поддерживает метод write_log(), записывающий событие в правильный файл дня в формате:
# [06:23:15] Произошедшее событие
# 6. Поддерживает метод clear_log(), который удаляет записи в файле текущего дня.
# 7. Поддерживает метод get_logs(), возвращающий записи из файла текущего дня в виде списка (один
# элемент списка — запись одного события).
# 8. Поддерживает метод get_last_event(), который возвращает запись о последнем событии.
# 9. Поддерживает метод get_all_logs(), который возвращает список всех файлов лога.
# Предусмотреть крайние ситуации при которых возможен вылет. Исключить возможные ошибки
# конструкциями try-except и raise exception.
from datetime import date
from dateutil.relativedelta import relativedelta
import os


class Logger:

    def __init__(self, event):
        self.event = event
        time = Logger.get_time()
        with open('Log_' + time, 'a', encoding='UTF-8') as f:
            f.write('[' + time + ']' + ' ' + event + '\n')

    def write_log(self, event):
        pass

    @staticmethod
    def get_time(value=0):
        time = date.today() + relativedelta(days=value)
        current_time = time.strftime("%m.%d.%Y")
        return current_time

    def clear_log(self):
        time = Logger.get_time()
        f = open('Log_' + time, 'w+')
        f.seek(0)
        f.close()

    def get_logs(self):
        time = Logger.get_time()
        with open('Log_' + time, 'r', encoding='UTF-8') as f:
            return f.readlines()


    def get_last_event(self):
        time = Logger.get_time()
        with open('Log_' + time, 'r', encoding='UTF-8') as f:
            return f.readlines()[-1]

# cat = Logger('33r3')
cat = Logger('234242')
print(cat.get_time())
print(cat.get_logs())
print(cat.get_last_event())
