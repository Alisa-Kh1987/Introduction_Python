# Создайте функцию генератор чисел Фибоначчи


def fibonachi_gen(stop_generate: int):
    fibo_list = [0, 1] # первые два числа в последовательности Фибоначчи равны, соотв., 0 и 1. Они уже вкл.чены в список
    current_num = 0
    while current_num < stop_generate:
        yield fibo_list[-1]
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
        current_num += 1


for i in fibonachi_gen(10):
    print(i)