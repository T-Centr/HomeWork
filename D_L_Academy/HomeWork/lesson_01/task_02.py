# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


a = int(input('Введите переменную a: '))
b = int(input('Введите переменную b: '))
c = a
a = b
b = c

print(f'a = {a}, b = {b}')
