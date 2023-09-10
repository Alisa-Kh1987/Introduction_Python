# Создайте функцию генератор чисел Фибоначчи

def fibonachi_gen(stop_generate: int):
    list_fibo = [0, 1]
    current_number = 2  # первые два числа в последовательности Фибоначчи равны, соотв., 0 и 1. Они уже вкл.чены в список
    while current_number <= stop_generate:
        yield list_fibo[-2]
        list_fibo.append((current_number-1)+(current_number-2))
        current_number+=1

for number in fibonachi_gen(10):
    print(number)
