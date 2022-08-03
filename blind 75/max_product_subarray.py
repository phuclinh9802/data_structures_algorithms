def maxProduct(nums):
    # use dp approach 2 pointers max & min
    res = -float('Inf')
    maxTmp, minTmp = 1, 1

    for n in nums:
        if n == 0:
            max, min = 1, 1 # reset if current el is 0

        temp = max * n
        maxTmp = max(maxTmp * n, minTmp * n, n)
        minTmp = min(temp, minTmp * n, n)

        res = max(res, maxTmp)

    return res