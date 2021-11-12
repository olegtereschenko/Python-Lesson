a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class Matrix:
    def __init__(self, list_new):
        self.list_new = list_new

    def __str__(self):
        return '\n'.join(map(str, self.list_new))

    def __add__(self, other):
        c = []
        for i in range(len(self.list_new)):
            c.append([])
            for j in range(len(self.list_new[0])):
                c[i].append(self.list_new[i][j] + other.list_new[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f'Matrix 1\n{matrix_1}\n{"-" * 20}')
print(f'Matrix 2\n{matrix_2}\n{"-" * 20}')
print(f'matrix 1 + matrix 2\n{matrix_1 + matrix_2}')
