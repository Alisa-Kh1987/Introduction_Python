# 📌Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число. 
# 📌Обрабатывайте не числовые данные как исключения.

def input_number():
    while True:
        number = input('Введите целое или вещественное число: ')
        try:
            return int(number)
        except:
            try:
                return float(number)
            except:
                print('Это не число. Попробуйте еще раз')

print(input_number())