# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint, sample
import string


num_of_names = randint(3, 10)

vowels = 'aeiouv'

def write_names_in_file():
    names = []
    while len(names) < num_of_names:
        res = sample(string.ascii_lowercase, randint(4,7))
        if len(set(string.ascii_lowercase) & set(vowels)) > 0:
            names.append(''.join(res).title())