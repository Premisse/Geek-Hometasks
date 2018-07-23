# coding: UTF-8

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3


import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создать копию указанного файла")
    print("rm <file_name> - удалить указанный файл")
    print("cd <full_path> - изменить текущую директорию на указанную")
    print("ls - отобразить полный путь текущей директории")


def make_dir():

    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file():

    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    new_file = file_name + '_copy'
    try:
        shutil.copy(file_name, new_file)
        if os.path.exists(new_file):
            print("Копия файла {} создана".format(file_name))
        else:
            print('Возникли проблемы при копировании!')
    except FileNotFoundError:
        print("Такого файла нет!")

def del_file():

    if not file_name:
        print("Необходимо указать имя файла вторым параметром")

    make_sure = input("Вы уверены, что хотите удалить этот файл? y/n: ")
    try:
        if make_sure == "y":
            os.remove(file_name)
            print("Файл {} был удален".format(file_name))
        elif make_sure == "n":
            print("Хорошо, что передумали!")
        else:
            print("Неверная команда!")
    except FileNotFoundError:
        print("Указанного файла {} нет".format(file_name))

def change_dir():

    if not full_path:
        print("Необходимо указать путь к директории вторым параметром")
        return
    try:
        os.chdir(full_path)
        result = "Директория изменена"
        print(result)
    except FileNotFoundError:
        print("Неверно введена директория!")

def show_path():
    path = os.getcwd()
    print(path)

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": del_file,
    "cd": change_dir,
    "ls": show_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    full_path = sys.argv[2]
except IndexError:
    full_path = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")