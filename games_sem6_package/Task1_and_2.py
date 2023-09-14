# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# Улучшаем задачу 2.

# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from sys import argv
from random import randint


def guess(start_, stop_, tries):
    random_num = randint(start_, stop_)
    while tries > 0:
        user_num = int(input('Enter your number: '))
        if user_num == random_num:
            print('you win')
            break
        elif user_num > random_num:
            print('random number is less')
        else:
            print('random number is bigger')
        tries -=1
    else:
        print('game over')


# guess(0, 100, 12)
# if argv:
print(argv)