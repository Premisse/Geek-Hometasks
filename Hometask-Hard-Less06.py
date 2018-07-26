# coding: UTF-8

# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Factory:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def identificate(self):
        if type == "кукла":
            new_toy = Doll(self.name, self.color, self.type)
        elif type == "животное":
            new_toy = Animal(self.name, self.color, self.type)
        elif type == "персонаж":
            new_toy = Animate(self.name, self.color, self.type)
        return new_toy

    def buy_raw(self):
        print("Закупка сырья")

    def sewing(self):
        print("Пошив")

    def paint(self):
        print("Окраска")

class Doll():
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

class Animal():
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

class Animate():
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

name = input("Введите имя игрушки: ")
color = input("Введите цвет игрушки: ")
type = input("Введите тип игрушки, кукла/животное/персонаж: ")

a = Factory(name, color, type)
try:
    b = a.identificate()
    print("Создана игрушка типа - ", b.type)
except UnboundLocalError:
    print("Неверно введен тип игрушки!")