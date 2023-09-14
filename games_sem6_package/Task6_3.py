# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from random import choice
import random

_result_dict = {}


def stor_of_puzzles():
    dict_puzzles = {"Зимой и летом одним цветом": ['ель', 'доллар', 'труп'], 
                    "Висит груша - нельзя скушать": ['лампочка', 'сайт', 'труп'],
                    "Без окон, без дверей - полна горница людей": ['огурец', 'сейф', 'вагон метро в час-пик']}
    
    result = choice(list(dict_puzzles))
    return result, dict_puzzles[result]

def save_result(puzzles: str, tries: int):
    _result_dict[puzzles] = tries

def show_results():
    
        return '\n'.join([f'Загадка "{puzzles}" отгадана с {tries} попытки' 
                        for puzzles, tries in _result_dict.items()])

def guess_puzzle(count):
    for _ in range(count):
        puzzles, answers = stor_of_puzzles()
        tries = random.randint(2, 5)
        print(puzzles)
        print(f'У тебя {tries} попыток\n')
        i = 0
        
        while count < tries:
            user_answer = input('Please input your answer: \n').lower()
            if user_answer in answers and user_answer == answers[0]:
                print(f'You win. {count+1} попытка\n')
                save_result(puzzles, count)
                break
            else:
                print("wrong answer. try again\n")
                count +=1
                print(f'У тебя осталось {tries - count} попыток\n')
        else:
            print(f'Game over! you are luser. Correct answer was {answers[0]}\n')


guess_puzzle(4)
print(show_results())

