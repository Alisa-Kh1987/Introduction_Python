# ✔Функция получает на вход список чисел.
# ✔Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

import random

int_list = [random.randint(0, 50) for i in range(10)]
print(f'Исходный список = {int_list}')


def buble_sort(list_):
    for i in range(len(list_)):
        for j in range(0, len(list_)-i-1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]


buble_sort(int_list)
print(f'Отсортированный список = {int_list}')
