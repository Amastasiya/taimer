# Сделать таймер отсчета времени до нового года

# 1 Взять библиотеку datetime
# 2 с помощью этой библиотеке получить текущую дату и время
# 3 Вычислить количество секунд до НГ вывести в консоле

import datetime
import time

#def now_day():
    #now = datetime.datetime.today()
    #print("Сегодня", now)

#now = now_day()

def new_year():
    while True:
        now = datetime.datetime.now()
        #print("Сегодня сейчас", now)
        new_year = datetime.datetime(2023, 1, 1)
        counter_time = new_year - now
        print(counter_time.days*24*60*60 + counter_time.seconds) # секунды
        time.sleep(5)
        print("Осталось до Нового года", counter_time)

new_year()












