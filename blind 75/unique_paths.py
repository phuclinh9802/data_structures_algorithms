def unique_path(m, n):
    row = [1] * n # last row

    for i in range(m - 1): # loop from second to last row
        temp = [1] * n # set second to last row cells to 1
        for j in range(n - 2, -1, -1): # go bottom up, start from col n - 2 for every iteration
            temp[j] = temp[j + 1] + row[j] # current cell = cell at right + cell at bottom of current cell
        # move old row up 1 row by setting old row to temp row (after calculated)
        row = temp
    return row[0] # row at [0][0] will be the final answer since we move bottom up