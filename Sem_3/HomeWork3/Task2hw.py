# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

import random

my_list = [random.randint(0, 10) for i in range(10)]
print(f'my_list = {my_list}')

duplicate_list = []

for i in my_list:
    count = my_list.count(i)
    if count >=2:
        duplicate_list.append(i)

print(f'result_list = {list(set(duplicate_list))}')