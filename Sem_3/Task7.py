# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

my_str = input('Введите строку текста: ')
new_dict = {}
new_dict_2 = {}

for i in my_str:
    if i in new_dict:
        new_dict[i] +=1
    else:
        new_dict[i] = 1

print(new_dict)

for i in set(my_str):
    if i not in new_dict_2:
        new_dict_2[i] = my_str.count(i)

print(new_dict_2)
