def sudoku(matrix):
    rows = {}
    cols = {}

    for row in range(1, 10):
        for col in range(1, 10):
            for num in range(1, 10):
                r = []
                quad = ((row - 1)/3) * 3 + (col - 1)/3 + 1
                if row == col:
                    r.append(0)