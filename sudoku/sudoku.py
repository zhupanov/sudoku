#!/usr/local/bin/python3

def top_left(x):
    return (x // 3) * 3

class Sudoku:
    def __init__(self):
        given = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        # make every element be a set of numbers 1..9
        self.m = [[set(range(1, 10)) for i in range(9)] for i in range(9)]

        # replace given numbers x by set(x)
        for row in range(9):
            for column in range(9):
                element = given[row][column]
                if element != 0:
                    self.m[row][column] = {element}

        for row in range(9):
            for column in range(9):
                cell = self.m[row][column]
                assert(len(cell) == 1 or len(cell) == 9)

        assert(not self.is_solved())

    def is_solved(self):
        for row in range(9):
            for column in range(9):
                cell = self.m[row][column]
                if len(cell) != 1:
                    return False
        return True

    def output(self):
        for i in range(9):
            if i in (3, 6):
                print('-' * (9 + 8 + 4))
            for j in range(9):
                if j in (3, 6):
                    print('|', end=' ')
                cell = self.m[i][j]
                if len(cell) == 1:
                    print(list(cell)[0], end=' ')
                else:
                    print('0', end=' ')
            print()

    def simplify_row(self, row, x):
        for column in range(9):
            cell = self.m[row][column]
            if len(cell) > 1:
                cell.discard(x)

    def simplify_column(self, column, x):
        for row in range(9):
            cell = self.m[row][column]
            if len(cell) > 1:
                cell.discard(x)

    def simplify_quadrant(self, row, column, x):
        qr = top_left(row)
        qc = top_left(column)
        quadrant_elements = (
            (qr,   qc), (qr,   qc+1), (qr,   qc+2),
            (qr+1, qc), (qr+1, qc+1), (qr+1, qc+2),
            (qr+2, qc), (qr+2, qc+1), (qr+2, qc+2),
        )
        for (r, c) in quadrant_elements:
            cell = self.m[r][c]
            if len(cell) > 1:
                cell.discard(x)

    def simplify(self):
        for row in range(9):
            for column in range(9):
                cell = self.m[row][column]
                if len(cell) == 1:
                    x = list(cell)[0]
                    self.simplify_row(row, x)
                    self.simplify_column(column, x)
                    self.simplify_quadrant(row, column, x)
                    self.m[row][column] = {x}  # restore the cell after simplify


s = Sudoku()
while not s.is_solved():
    s.simplify()
s.output()
