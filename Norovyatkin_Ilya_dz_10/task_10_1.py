from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        m_rows = len(self.matrix)
        self.matrix_size = frozenset([(m_rows, len(row)) for row in self.matrix])

        if len(self.matrix_size) != 1:
            raise ValueError("Неправильный размер матрицы")

    def __str__(self):
        return '| ' + ' |\n| '.join([' '.join(map(str, row)) for row in self.matrix]) + ' |'

    def __add__(self, matrix_1: "Matrix"):
        if not isinstance(matrix_1, Matrix):
            raise TypeError(f"'{matrix_1.__class__.__name__}' "
                            f"неправильный тип объекта")
        if self.matrix_size != matrix_1.matrix_size:
            raise ValueError(f'Размеры матриц не совпадают')

        result = []

        for item in zip(self.matrix, matrix_1.matrix):
            result.append([sum([a,b]) for a, b in zip(*item)])

        return Matrix(result)

if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix, '\n')
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(second_matrix, '\n')
    """
    | 6 5 |
    | 4 3 |
    | 2 1 |
    """
    
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """