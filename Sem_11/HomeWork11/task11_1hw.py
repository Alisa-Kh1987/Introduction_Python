# Создайте класс Матрица. Добавьте методы для: 
# вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:
    def __init__(self, matrix: list[list]):
        self.value = matrix
        self.length = len(matrix)
        self.height = len(matrix[0])

    def __str__(self):
        return "\n".join(str(i) for i in self.value)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.value[i][j] == other.value[i][j])
                return all(result)
        return False
    
    def __lt__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.value[i][j] < other.value[i][j])
                return all(result)
        return False
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = [[] for i in range(self.length)]
                for i in range(self.length):
                    for j in range(self.height):
                        result[i].append(self.value[i][j] + other.value[i][j])
                return Matrix(result)
            
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.length:
                result = [[sum(m * n for m, n in zip(self_row, other_col))
                            for other_col in zip(*other.value)]
                            for self_row in self.value]
            elif self.length == other.height:
                result = [[sum(m * n for m, n in zip(self_col, other_row))
                            for self_col in zip(*self.value)]
                            for other_row in other.value]
            return Matrix(result)
        return False
    
    

if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f'matrix_1: ')
    print(matrix_1)
    print()
    print(f'matrix_2: ')
    print(matrix_2)
    print()
    print(f'matrix_3: ')
    print(matrix_3)
    print()
    print(f'Равенство матриц № 2 и № 3: {matrix_2 == matrix_3}')
    print(f'Равенство матриц № 1 и № 3: {matrix_1 == matrix_3}')
    print(f'Матрица № 1 меньше матрицы № 2: {matrix_1 < matrix_2}')
    print(f'Матрица № 3 больше матрицы № 2: {matrix_3 > matrix_2}')
    print()
    print(f'Cложение матриц:')
    print(matrix_1 + matrix_2)
    print()
    print(f'Умножение 2х матриц: ')
    print(matrix_2 * matrix_3)
