# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

things = {'palatka': 4.0, 'spalnik': 2.0, 'kovrik': 1.0, 'kotelok': 0.2, 'eda': 3.0, 'voda': 1.5, 'spichki': 0.05, 'kompas': 0.1, 'pila': 0.3, 'tent': 1.1, 'antikomarin': 0.3, 'fonarik': 0.1, 'topor': 2.0, 'gorelka': 1.0, 'gas': 1.0}
backpack_weight = 13.5
# поиск допустимой комбинации:
backpack_things = {}
for key, value in things.items():
    if backpack_weight - value >= 0:
        backpack_things[key] = value
        backpack_weight = backpack_weight - value

print(sum(backpack_things.values()))
print(backpack_things)








