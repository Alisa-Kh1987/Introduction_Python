# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import math
from fractions import Fraction

# Основная программа ("без модуля fractions")
drob1 = str(input('Введите строку вида "a/b": '))
drob2 = str(input('Введите строку вида "c/d": '))
a, b = map(int, drob1.split("/"))
c, d = map(int, drob2.split("/"))

# Сложение дробей
nom_summ = (a*d) + (b*c)
denom_summ = b*d
nod1 = math.gcd(nom_summ, denom_summ)

# Умножение дробей
nom_mult = a*c
denom_mult = b*d
nod2 = math.gcd(nom_mult, denom_mult)

# Проверка через модуль fractions с последующим выводом результатов - как основного блока вычислений, так и через модуль fractions:

drob1_fract = Fraction(a, b)
drob2_fract = Fraction(c, d)

if denom_summ ==0 or denom_mult == 0:
    raise ZeroDivisionError("Деление на ноль невозможно")
else:
    print(f"Cумма дробей {drob1} и {drob2} - {nom_summ//nod1}/{denom_summ//nod1}")
    print(f"Cумма дробей_fractions {drob1_fract} и {drob2_fract} - {drob1_fract+drob2_fract}")
    print()
    print(f"Произведене дробей {drob1} и {drob2} - {nom_mult//nod2}/{denom_mult//nod2}")
    print(f"Произведение дробей_fractions {drob1_fract} и {drob2_fract} - {drob1_fract*drob2_fract}")