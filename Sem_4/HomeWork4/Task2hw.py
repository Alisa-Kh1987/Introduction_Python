# # Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# # переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# попробовала сделать лекции 5 с проверкой на хешируемость ключа. Надеюсь, что верно.
def new_dict_function(**kwargs):
    return {value if value.__hash__ != None else str(value): key for key, value in kwargs.items()}


print(new_dict_function(name='Alisa', age='18 мне уже', job='environmental engineer', day=3, month=11, new_year=[1, 1, 23]))
