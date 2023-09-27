# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Dog:
    def __init__(self, name:str, age: int, **kwargs):
        self._name = name
        self._age = age
        self._special = kwargs.get('breed', None)

    def get_special(self):
        return self._special

class Cat:
    def __init__(self, name:str, age: int, **kwargs):
        self._name = name
        self._age = age
        self._special = kwargs.get('color', None)

    def get_special(self):
        return self._special

class Fish:
    def __init__(self, name:str, age: int, **kwargs):
        self._name = name
        self._age = age
        self._special = kwargs.get('habitat', None)

    def get_special(self):
        return self._special
    
sponki = Dog('Спонки', 3, breed = 'Овчарка')
tom = Cat('Том', 3, color = 'Серый')
dory = Fish('Дори', 1, habitat = 'Дом')

for animal in (sponki, tom, dory):
    print(animal.get_special())

# вновь созданный класс принимает тип животного (один из созданных классов)
## вариант 1, как я поняла - скорее всего, неверное понимание ДЗ
class Animal_fabric(Dog):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, **kwargs)