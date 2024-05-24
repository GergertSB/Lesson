# Функции в Python. Функция с параметром. Документирование функции

def say_hello(): # обычная функция
    print('Hello')

say_hello() # вызываем функцию
say_hello() # вызываем её ещё раз
say_hello() # и ещё раз

# пример принимающей функции

def say_hello(name): # принимающая функция
    print('Hello', name)

say_hello('Denis')
say_hello('Max')
say_hello('Anton')

# пример возвращающей функции

import random # подключаем библиотеку
def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win = random.choice(tickets) # вызываем в случайном порядке выигрышный билет
    return win # функция возвращает нам переменную в которой находится выигрышный билет

win = lottery() # создаем переменную и сохраняем в неё вызов функции
print(win) # выводим на экран нашу переменную

# пример принимающей и возвращающей функций совместно

import random
def lottery(mon, thue): # функция с двумя принимающими
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets) # вызываем первый раз значение
    tickets.remove(win1) # удаляем из списка выбранное значение, не может билет выиграть 2 раза
    win2 = random.choice(tickets) # вызываем второй раз значение из списка
    print(mon, thue)
    return win1, win2

win1, win2 = lottery(mon: 'Mon', thue: 'Thue')
print(win1, win2)
