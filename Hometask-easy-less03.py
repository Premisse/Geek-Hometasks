# coding: UTF-8

# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def ident_info (name, age, city):
    info = '{} {} год(а), проживает в городе {}'.format(name, age, city)
    print(info)

name = input("Введите имя: ")
age = input("Введите возраст: ")
city = input("Введите город: ")

ident_info(name, age, city)

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def compare(a, b, c):
    return max(a, b, c)

a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

print(compare(a, b, c))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_length(*args):
    return max(args)

print("Самое длинное слово: ", max_length("картина", "корзина", "картонка", "и", "маленькая", "собачонка"))