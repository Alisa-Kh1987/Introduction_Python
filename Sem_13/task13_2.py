# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


from typing import Any


def our_get(dct: dict, key: Any, default_value: Any = None) -> Any:
    try:
        return dct[key]
    except KeyError:
        return default_value
    except TypeError:
        return 'Ошибка типа ключа!'

print(our_get(dict_1, [1,2]))
print(our_get(dict_1, 1))
print(our_get(dict_1, 3, default_value='Пусто'))