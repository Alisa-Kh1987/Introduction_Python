# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

import random


my_list = [random.randint(0, 10) for i in range(20)]
random.seed()
print(f'my_list = {my_list}')

res_list = []

for i in range(len(my_list)):
    if my_list[i] % 2 ==1:
        res_list.append(i+1)

print(f'res_list = {res_list}')