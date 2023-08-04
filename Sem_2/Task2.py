# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys
data = [1, 2.43, True, 43, False, 1, "three"]
for i in range(len(data)):
    print(i+1)
    print(data[i])
    print(id(data[i]))
    print(sys.getsizeof(data[i]))
    print(hash(data[i]))
    if isinstance(data[i], int):
        print(isinstance(data[i], int))
    print()
    if isinstance(data[i], str):
        print(isinstance(data[i], str))
