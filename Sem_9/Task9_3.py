import json
import os


def json_safe(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not os.path.exists(f'{func.__name__}.json'):
            # print('Зашел')  # принтовать "Зашел" можно для отслеживания, выполняется или нет та или иная строка кода, тем самым выявлять ошибку
            with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f:
                json.dump({result: (args, kwargs)}, f, indent=4, ensure_ascii=False)

        else:
            with open(f'{func.__name__}.json', 'r', encoding='utf-8') as f_read:
                json_data = json.load(f_read)
                print(json_data)
            with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f_write:
                json_data[result] = (args, kwargs)
                json.dump(json_data, f_write, indent=4, ensure_ascii=False)

        return result

    return wrapper


@json_safe
def function_(a, b):
    return a + b


function_(337, 499)
function_(0, 555)
function_(a=23432, b=5645655)
function_(4560, b=564555)