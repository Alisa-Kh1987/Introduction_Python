# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))
res_16 = ""
num16 = num
while num16 > 0:
    res_16 = str(num16 % 16) + res_16
    num16 //= 16
print(res_16, hex(num).replace("0x", ''))