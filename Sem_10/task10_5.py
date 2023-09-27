# 📌Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
# 📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
# 📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

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
    
sponki = Dog('Спанки', 3, breed = 'Овчарка')
tom = Cat('Том', 3, color = 'Серый')
dory = Fish('Дори', 1, habitat = 'Дом')

for animal in (sponki, tom, dory):
    print(animal.get_special())