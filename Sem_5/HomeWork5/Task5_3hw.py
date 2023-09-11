# Создайте функцию генератор чисел Фибоначчи


def fibonachi_gen(stop_generate: int):
    fibo_nums = [0, 1] # первые два числа в последовательности Фибоначчи равны, соотв., 0 и 1. Они уже вкл.чены в список
    current_num = 0
    while current_num < stop_generate:
        yield fibo_nums[-1]
        fibo_nums.append(fibo_nums[-1] + fibo_nums[-2])
        current_num += 1


for i in fibonachi_gen(10):
    print(i)