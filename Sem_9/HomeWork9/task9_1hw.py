#Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import random
import math
import functools


# Нахождение корней квадратного уравнения
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        result = (round((-b + math.sqrt(discriminant)) / (2*a), 2), round((-b - math.sqrt(discriminant)) / (2*a), 2))
    elif discriminant == 0:
        result = -b/2*a
    else:
        print('Вещественных корней нет')
    return result


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def generate_csv_file(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(random.randint(100, 1001)):
            writer.writerow([random.randint(0,100) for _ in range(3)])


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def from_csv_decorator(func):
    @functools.wraps(func)
    def wrapper(filename):
        results = []
        with open(filename,'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                results.append(func(a, b, c))
        return results
    return wrapper

# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.json', 'a', encoding='utf-8') as f:
            json.dump({'func': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result}, f)
        return result
    return wrapper