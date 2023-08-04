# Задание №5
# ✔ Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# ✔ Используйте комплексные числа для извлечения квадратного корня.

a, b, c = int(input('Введите a: ')), int(input('Введите b: ')), int(input('Введите c: '))
discriminant = b**2 - 4*a*c

if discriminant == 0:
    res = -b/(2*a)
elif discriminant > 0:
    res = ((-b+discriminant**0.5)/(2*a), (-b-discriminant**0.5)/(2*a))
else:
    discriminant = complex(discriminant, 0)
    res = ((-b+discriminant**0.5)/(2*a), (-b-discriminant**0.5)/(2*a))
print(res)