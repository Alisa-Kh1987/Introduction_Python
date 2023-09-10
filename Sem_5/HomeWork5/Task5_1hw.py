# # # ✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# # Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def file_info(path_:str) -> tuple:
    file_path, file_extenc = os.path.splitext(path_)
    file_name = 'Task5_1hw.py'[:-3]
    return file_path, file_name, file_extenc


print(file_info('C:\\Users\\petru\\OneDrive\\Рабочий стол\\GB\\Introduction_to_Python\\Task5_1hw.py'))