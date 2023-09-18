# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint, sample
import string


num_of_names = randint(3, 10)

vowels = 'aeiouv'
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import randint

num_of_names = randint(3,10)
vowels = 'aeiouv'
size = randint(4,7)

def write_names_in_file():
    names = []
    while len(names) < num_of_names:
        res = sample(string.ascii_lowercase, size)
        if len(set(string.ascii_lowercase) & set(vowels)) > 0:
            names.append(''.join(res).title())
            print(f'{names = }')

    with open('file_names.txt', 'a', encoding = 'utf-8') as f:
        f.writelines('\n'.join(names))
    

write_names_in_file()