# ✔Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке. 
# ✔Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения. 
# ✔Для вывода результата используйте «принт» без перехода на новую строку.

print('\n'.join(''.join([(('\t'.join([f'{i:>2} x {j:>2} = {i*j:>2}' for i in range(2+k,6+k)])) + '\n') for j in range(2,11)]) for k in [0,4]))