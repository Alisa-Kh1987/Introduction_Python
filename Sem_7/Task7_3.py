import json
import os


def open_files(file_name1, file_name2):
    names, numbers = None, None
    with (
        open(file_name1, 'r', encoding='utf-8') as f1, 
        open(file_name2, 'r', encoding='utf-8') as f2
    ):
        numbers = f2.readlines()
        names = f1.readlines()

        numbers = list(map(lambda x: int(x.strip().split(' | ')[0]) * float(x.strip().split(' | ')[1]), numbers))
        names = list(map(lambda x: x.strip(), names))
        print(f'{numbers = } \n {names = }')
        list_to_write = list(zip(names, numbers))
        print(f'{list_to_write = }')

        with open("results.txt", 'a', encoding='utf-8') as f:
            for st in list_to_write:
                if st[1] > 0:
                    f.write(f'{st[0].upper()} -> {round(st[1])} \n')
                else:
                    f.write(f'{st[0].lower()} -> {abs(st[1])} \n')

open_files('file_names.txt', 'Task7_1.txt')

def create_json(list_, file_path):
    dict_ = None
    with open('results.txt', 'r', encoding='utf-8') as f:
        names = f.readlines()
        for name in names:
            name = name.strip().split(' -> ')
            dict_[name[0]] = float(name[1])
        print(dict_)

    with open(file_path, 'a', encoding='utf-8') as f:
        json.dump(dict_, f, indent=4, ensure_ascii=False)
        

create_json(os.path.join(os.getcwd(), 'first_json.json'))