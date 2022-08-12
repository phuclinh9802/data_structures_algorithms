def setZeroes(matrix):
    # we alter the matrix in place, and only need O(1) extra memory to check for 0 in the first row

    isZero = False
    ROWS, COLS = len(matrix), len(matrix[0])

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    isZero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if isZero:
        for c in range(COLS):
            matrix[0][c] = 0

