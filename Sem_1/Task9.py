# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for k in [0, 1]:
    for j in range(2, 11):
        row = []
        for i in range(2 + k * 4, 6 + k * 4):
            row.append(f'{i:^3} X {j:^3} = {j * i:^3}')
        print('\t\t\t'.join(row))
    print('\n')