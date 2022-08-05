def counting_bits(n):
    # brute force:
    res = [0]
    count = 0

    # n = 5 ->
    # n = 1 -> append count = 1
    # n = 2 -> append count = 1
    # n = 3 -> append count = 2
    # ...

    for i in range(1, n + 1):
        j = i
        count = 0
        while j > 0:
            count += j % 2
            j = int(j // 2)

        res.append(count)

    return res



    # dp approach
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp