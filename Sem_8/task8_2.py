# Задание № 2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import os
import json


def create_json(path: str = 'users.json'):
    users_data = {}
    while True:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                users_data = json.load(file)
        id_list = [user[1] for user in users_data.values()]
        name = input('Введите имя пользователя: ')
        if not name:
            break
        while True:
            u_id = input('Введите личный ID: ')
            if u_id.isdigit():
                if int(u_id) not in id_list:
                    u_id = int(u_id)
                    break
                else:
                    print(f'ID {u_id} уже занят. Используйте другой')

        u_lvl = int(input('Введите уровень доступа: '))
        if u_lvl in users_data:
            users_data[u_lvl].append((name, u_id))
        else:
            users_data[u_lvl] = ((name, u_id))

create_json()
