class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        try:
            mat = [
                [int(self.matrix[line][item]) + int(other.matrix[line][item]) for item in range(len(self.matrix[line]))]
                for line in range(len(self.matrix))]
            return Matrix(mat)
        except IndexError:
            return f'разные размеры матриц'

    def __str__(self):
        return '\n'.join('\t'.join([str(item) for item in line]) for line in self.matrix)


matrix_1 = Matrix([[2, 3, 4], [8, 9, 10]])
matrix_2 = Matrix([[5, 6, 7], [1, 2, 3]])
matrix_sum = matrix_2 + matrix_1
print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_sum)
