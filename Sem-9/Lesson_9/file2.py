# def add_str(a:str, b: str) -> str:
#     return a + ' ' + b


# print(add_str('hello', 'world'))

# перепишем через замыкание функцию, написанную выше

from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]: # add-one - принимает строку, возвр функцию, которая в свою очередь также принимает на вход строку и возвращает строку
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    
    return add_two_str


print(add_one_str('Hello')('world'))