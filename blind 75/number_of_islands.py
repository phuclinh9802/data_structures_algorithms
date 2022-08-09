import collections

def number_of_islands(grid):
    # this problem can be approached by dfs/bfs approach

    # base case
    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])

    visit = set()
    island = 0

    def bfs(r, c):
        # since bfs, need a queue
        # append r, c immediately
        queue = collections.deque()
        queue.append((r, c))
        visit.add((r,c))

        while queue: # check until queue is empty after popping left
            row, col = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                # store current cell by directions
                r, c = row + dr, col + dc
                # check if satisfies conditions
                # 1. in bound
                # 2. current cell = 1
                # 3. (r,c) not visited yet
                if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r, c) not in visit:
                    # add to visit & queue
                    visit.add((r, c))
                    queue.append((r,c))

        # outside of bfs, do nested loop and check if satisfies conditions cell = 1 & r, c not visited yet
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1

        return island



