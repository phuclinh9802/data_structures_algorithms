def pacific_atlantic(heights):
    # this is a 2d list to traverse from cell to cell, we can use dfs approach
    # with 2 sets pac and atl to check if (r, c) is visited
    # init ROWS and COLS constants
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()
    result = []

    # do dfs nested function with params: r, c, set, and prev cell
    def dfs(r, c, visit, prev):
        # base case:
        # 1. out of bounds
        # 2. (r, c) exists in set
        # 3. current cell < prev cell
        # -> return
        if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or heights[r][c] < prev:
            return

        visit.add((r, c))
        # dfs
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])

        return

    # go through rows
    for r in range(ROWS):
        # dfs loop
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    # go through cols
    for c in range(COLS):
        # dfs loop
        dfs(0, c, pac, heights[c][0])
        dfs(ROWS - 1, c, pac, heights[ROWS - 1][c])

    # nested loop to check if cell in pac and atl
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                result.append([r, c])

    return result
