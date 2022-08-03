def coin_change_2(A, B):
    dp = [[0] * (len(A)+1) for _ in range(len(B)+1)]
    dp[0] = [1] * (len(A) + 1)

    for i in range(1, B+1):
        for j in range(len(A) - 1, -1, -1):
            dp[i][j] = dp[i][j+1]
            if i - A[j] >= 0:
                dp[i][j] += dp[i - A[j]][i]

    return dp[B][0]


# We use grid (coins as column, amount as row) then go bottom-up from [1][len(A)-1] to [B][0]