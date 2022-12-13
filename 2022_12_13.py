# Сделать таймер отсчета времени до нового года

# 1 Взять библиотеку datetime
# 2 с помощью этой библиотеке получить текущую дату и время
# 3 Вычислить количество секунд до НГ вывести в консоле

import datetime

def now_day():
    now = datetime.datetime.today()
    print("Сегодня сейчас", now)
    return now
now = now_day()

def new_year_second(now):
    new_year = datetime.datetime(2023, 1, 1)
    print(new_year)
    counter_time = new_year - now
    return counter_time





