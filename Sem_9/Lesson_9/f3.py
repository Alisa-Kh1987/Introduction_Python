from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    
    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')
go = add_one_str('Едем, едем в соседнее село')

# созданы две переменные hello и bye и поместили в них результат работы функции add_one_str с разными
# аргументами: можно вызывать новые функции и получать объединённые строки передавая только окончание. 
# Первая часть строки оказалась замкнута в локальной области видимости. 
# И у каждой из двух новых функций область своя и начало строки своё.

print(hello('world!'))
print(hello('friend!'))
print(bye('wonderful world!'))
print(go('на дискотеку!'))
print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')
print(f'{type(go) = }, {go.__name__ = }, {id(go) = }')

# ОБЩИЙ ВИД

# def one(a): # внешняя функция
#     def two(b): #внутренняя функция
#         ...
#         return result
#     return two # внешняя функция возвращает внутреннюю функцию, внутренняя - результат


# closure = one(data) # результат работы внешней функции мы сохраняем в какой-то переменной, тем самым создаем замыкание - замыкаем внутреннюю функцию на какой-то переменной