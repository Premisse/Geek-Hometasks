# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import datetime

list = [2, -5, 8, 9, -25, 25, 4]
new_list = []
j = None

for i in list:
    if i > 0:
        j = math.sqrt(i)
        if j.is_integer():
            j = int(j)
            new_list.append(j)
    i += 1
print(new_list)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

my_date = '02.11.2013'
day = str(my_date[0:2])
month = my_date[3:5]
year = my_date[6:]
day_dict = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое', '12': 'двеннадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}
month_dict = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
text_date = []

for i in day_dict.keys():
    if i == day:
        text_date.append(day_dict[i])
        day = text_date[0]
    i = int(i)
    i += 1

for j in month_dict.keys():
     if j == month:
        text_date.append(month_dict[j])
        month = text_date[1]
     j = int(j)
     j += 1

print(day, month, year, 'года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

n = 10
random_list = []

for i in range(n):
    random_list.append(random.randint(-100, 100))
print(random_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

# var a

list_1 = [1, 2, 4, 5, 6, 2, 5, 2]
list_2 = list_1

for i in list_1:
    j = list_1.count(i)
    if j > 1:
        list_2.remove(i)

print(list_2)

# var b

list_1 = [1, 2, 4, 5, 6, 2, 5, 2]
list_2 = list_1

for i in list_1:
    j = list_1.count(i)
    if j > 1:
        list_2.remove(i)
        while i in list_2:
            list_2.remove(i)

print(list_2)