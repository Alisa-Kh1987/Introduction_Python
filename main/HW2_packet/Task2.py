# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_ALPHA = '0123456789ABCDEF'
num = int(input('Введите целое число: '))
res_16 = ""
num16 = num
while num16 > 0:
    # res_16 = str(num16 % 16) + res_16
    res_16 = HEX_ALPHA[num16 % 16] + res_16
    num16 //= 16
print(hex(num)[2:])