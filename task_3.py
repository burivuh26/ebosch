class Cell:
    def __init__(self, param):
        self.param = param

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.param // rows)]) + '\n' + '*' * (self.param % rows)

    def __str__(self):
        return f"{self.param}"

    def __add__(self, other):
        return f'сумма - {self.param + other.param}'

    def __sub__(self, other):
        return f"разница - {self.param - other.param}"

    def __mul__(self, other):
        return f"произведение - {self.param * other.param}"

    def __floordiv__(self, other):
        return f"частное при делении - {self.param // other.param}"


cell_1 = Cell(57)
cell_2 = Cell(13)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
