# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

# задача с семинара:
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

# закомментировала вывод задачи с семинара
#     
# sponki = Dog('Спонки', 3, breed = 'Овчарка')
# tom = Cat('Том', 3, color = 'Серый')
# dory = Fish('Дори', 1, habitat = 'Дом')

# for animal in (sponki, tom, dory):
#     print(animal.get_special())
    
# дорабатываем задачу с семинара (создаем класс-фабрику):
class Animal_fabric:
    def animal_from_factory(self, animal_type: str, name: str, age: int, **kwargs):
        if animal_type.lower() == 'dog':
            return Dog(name, age, **kwargs)
        elif animal_type.lower() == 'cat':
            return Cat(name, age, **kwargs)
        elif animal_type.lower() == 'fish':
            return Fish(name, age, **kwargs)
        else:
            return (f'Ошибка ввода типа животного')
        
animal = Animal_fabric()
dog = animal.animal_from_factory('dog', 'Komissar_Rex', 3, breed = "Horoshiy mal'chik")
cat = animal.animal_from_factory('cat', 'Kot Boris', 2, color = 'White')
fish = animal.animal_from_factory('fish', 'Guppi', 1, habitat = 'Skovorodka')

print(dog.get_special())
print(cat.get_special())
print(fish.get_special())




