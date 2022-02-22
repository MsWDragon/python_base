class Cell:

    def __init__(self, cells):
        self.cells = cells
        self.simbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cells}')

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"действие допустимо только для экземпляров того же класса")
        if (self.cells - other.cells) < 0:
            raise ValueError(f"недопустимая операция")
        return Cell(abs(self.cells - other.cells))

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"действие допустимо только для экземпляров того же класса")
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"действие допустимо только для экземпляров того же класса")
        x = int(self.cells / other.cells)
        return Cell(x)

    def __floordiv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"действие допустимо только для экземпляров того же класса")
        return Cell(self.cells // other.cells)

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f"действие допустимо только для экземпляров того же класса")
        return Cell(abs(self.cells + other.cells))

    def make_order(self, number: int):
        x = self.cells
        str_1 = ''
        while x > 0:
            for k in range(1,number+1):
                str_1+= self.simbol
                x -= 1
                if x <= 0:
                    break
            str_1+='\n'
        return str_1



if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса