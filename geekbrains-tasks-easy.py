__author__ = 'Евгения Комар'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

a = int(input("Введите любое целое число: "))

while a != 0:
    b = a % 10
    a = a // 10
    print(b)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

c = int(input("Введите число c: "))
d = int(input("Введите число d: "))

e = c
c = d
d = e

print("Число с =: ", c)
print("Число d =: ", d)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

r = int(input("Сколько Вам лет? "))

if r >= 18:
    print("Доступ разрешен!")
else:
    print("Извините, пользование данным ресурсом только с 18 лет!")