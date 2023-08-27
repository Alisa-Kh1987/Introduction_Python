# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.


import random

# my_list = [random.randint(0, 10) for i in range(10)]
# print(f'my_list = {my_list}')
# result_list = set(my_list)
# print()
# print(f'result_list = {result_list}')

my_list = [random.randint(0, 10) for i in range(10)]
print(f'my_list = {my_list}')

res_list = []
for i in my_list:
    if i not in res_list:
        res_list.append(i)

print(f'res_list = {res_list}')