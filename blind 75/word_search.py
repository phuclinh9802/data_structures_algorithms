class Solution:
    def word_search(self, board, word):
        # dfs
        # init length as rows/cols
        ROWS, COLS = len(board), len(board[0])
        # init a set to check for tuple (r,c) existence
        path = set()

        # nested function dfs, i is the current index of word variable
        def dfs(r, c, i):
            # base case
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= len(ROWS) or c >= len(COLS) \
                or word[i] != board[r][c] or (r, c) in path:
                return False

            # else, proceed to dfs
            path.add((r, c))
            res = dfs(r, c + 1, i + 1) or \
                dfs(r, c - 1, i + 1) or \
                dfs(r + 1, c, i + 1) or \
                dfs(r - 1, c, i + 1)
            path.remove((r, c))


            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False

