def open_files(file_name1, file_name2):
    names, numbers = None, None
    with (
        open(file_name1, 'r', encoding='utf-8') as f1, 
        open(file_name2, 'r', encoding='utf-8') as f2
    ):
        numbers = f1.readlines()
        names = f2.readlines()

        numbers = list(map(lambda x: int(x.strip().split(' | ')[0]) * float(x.strip().split(' | ')[1])))
        names = list(map(lambda x: x.strip(), names))
        print(f'{numbers = } \n {names = }')
        list_to_write = list(zip(names, numbers))
        print(f'{list_to_write = }')
        with open("results.txt", 'a', encoding='utf-8') as f:
            for st in list_to_write:
                f.write(f'{st} + \n')

open_files('file_names.txt', 'Task7_1.txt')

    