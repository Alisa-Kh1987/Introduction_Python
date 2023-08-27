# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

new_tuple = (2, 3.14, [5, 7], 'hello', 37, 1.5, 'New Year', '!!!')

new_dict = {}

for i in new_tuple:
    if type(i) not in new_dict:
        new_dict[type(i)] = [i]
    else:
        new_dict[type(i)].append(i)

print(new_dict)

