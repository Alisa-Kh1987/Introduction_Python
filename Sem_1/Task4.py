# Работа в консоли в режиме интерпретатора Python.
# Решите квадратное уравнение 5x2-10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.
# *Попробуйте решить уравнения с другими значениями a, b, c.

from tkinter import DoubleVar


a, b, c = int(input('Введите a: ')), int(input('Введите b: ')), int(input('Введите c: '))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    x1 = (-b+discriminant**0.5)/(2*a)
    x2 = (-b-discriminant**0.5)/(2*a)
    print(f'x1 = {round(x1, 2)}', ",", (f'x2 = {round(x2, 2)}')) # чтобы вспомнить форму записи через f-строку и округление чисел
elif discriminant == 0:
    x = -b/2*a
    print(x)
else:
    print('Вещественных корней нет')
