# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"


age = int(input('Введите Ваш возраст: '))
if age >= 18:
    print('Доступ разрешен.')
else:
    print('Извините, пользоваться данным ресурсом можно только с 18 лет.')
