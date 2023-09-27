# 📌Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
# 📌У класса должны быть методы birthday для увеличения возраста на год, 
# full_name для вывода полного ФИО и т.п. на ваш выбор. 
# 📌Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.



import random


class Human:
    def __init__(self, last_name: str, first_name: str, age: int, patronymic: str = None):
        self._last_name = last_name
        self._first_name = first_name
        self._patronymic = patronymic
        self._age = age

    def birthday(self):
        self._age +=1

    def get_age(self):
        return self._age
    
    def full_name(self):
        return (f'{self._last_name}{self._first_name}{"" if self._patronymic is None else (self._patronymic + " ")} ему '
                f'{self._age} лет')
    
# alisa = Human('Худякова', 'Алиса', 35, patronymic='Александровна')
# stone = Human('Панфилов', 'Кирилл', 39)

# print(stone.full_name())
# print(alisa.full_name())
# stone.birthday()
# print(stone.full_name())

class Employee(Human):
    def __init__(self, last_name, first_name, age, patronymic):
        super().__init__(last_name, first_name, age, patronymic)
        self.u_id = str(random.randint(1, 999999)).zfill(0)
        self.lvl_access = int(self.u_id)%7

alisa = Employee('Худякова', 'Алиса', 35, 'Александровна')
print(alisa.u_id)
print(alisa.lvl_access)
    
