# ✔Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def input_str():
    new_str = input('Введите строку: ')
    new_set = [ord(i) for i in set(new_str)]
    return (sorted(new_set, reverse=True))


print(input_str())
