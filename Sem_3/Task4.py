# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды

import random


my_list = [random.randint(0, 10) for i in range(20)]
random.seed()
print(f'my_list = {my_list}')

my_set = set(my_list)
print(f'my_set = {my_set}')

for i in my_set:
    if my_list.count(i) ==2:
        my_list.remove(i)
        my_list.remove(i)

print(f'Список после удаления = {my_list}')

