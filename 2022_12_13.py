# Сделать таймер отсчета времени до нового года

# 1 Взять библиотеку datetime
# 2 с помощью этой библиотеке получить текущую дату и время
# 3 Вычислить количество секунд до НГ вывести в консоле

import datetime

now = datetime.datetime.today()
print("Сегодня", now)

second = now.second
print(second)

new_year = datetime.datetime(2023, 1, 1)
print(new_year)

counter_time = new_year - now
print(counter_time)




