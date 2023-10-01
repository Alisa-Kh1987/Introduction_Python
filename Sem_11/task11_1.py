# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from time import time

class MyString(str):
    

    def __new__(cls, st, author_name):
        instance = super().__new__(cls, st)
        instance.author_name = author_name
        instance.st = st
        instance.time_ = time()
        return instance

stroks = MyString('lalala', 'OOP')
print(f'{stroks = }, {stroks.author_name = }, {stroks.time_ = }')        