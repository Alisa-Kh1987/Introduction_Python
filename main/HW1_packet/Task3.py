# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

n = int(input('Введите число: '))
message = None
if 0 < n <= 100000:
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            message = "Число составное"
        else:
            message = "Число простое"
    print(message)
else:
    print("Неверный ввод. Число должно быть положительным и не больше 100000")
