# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

my_strt = 'fghfgfghfhfgfhgfukkn'
my_dict = {i: ord(i) for i in my_strt}
print(my_dict)

my_iter = iter(my_dict.items())
for _ in range(5):
    print(next(my_iter))

#если снова вызвать 11ю строку, то выведутся следующие 5 значений и т.д. пока не закончатся значения