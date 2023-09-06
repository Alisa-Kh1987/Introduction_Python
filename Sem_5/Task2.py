# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку. 

my_strt = 'fghfgfghfhfgfhgfukkn'
my_dict = {i: ord(i) for i in my_strt}
print(my_dict)

my_iter = iter(my_dict.items())
for _ in range(19):
    print()