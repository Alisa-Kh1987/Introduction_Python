# ✔ Напишите функцию для транспонирования матрицы

import numpy as np

# генерим случайную матрицу (размер 4х4)
my_matrix = np.random.randint(1, 10, size=(4,4))
print('Исходная матрица: ')
print(my_matrix)
print() 

# Транспонируем матрицу
# 1 способ - с помощью метода transpose() из библиотеки NumPy 
# def transp_matrica(my_matrix):
#     my_matrix_transp = my_matrix.transpose()
# #    
#     return my_matrix_transp

# print(f'Транспонированная матрица: ')
# print(transp_matrica(my_matrix))

# 2 способ - с использованием генератора списка и функции matrix()
## np.matrix - дл вывода не в одну строку, а в 2D-формвте

def transp_matrica(my_matrix):
    my_matrix_transp = np.matrix([[my_matrix[j][i] for j in range(len(my_matrix))] for i in range(len(my_matrix[0]))])
#    
    return my_matrix_transp

print(f'Транспонированная матрица: ')
print(transp_matrica(my_matrix))