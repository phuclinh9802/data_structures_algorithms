def longest_consecutive_sequence(nums):
    # init res, set
    res = 0
    num_set = set(nums)

    for n in nums:
        if n - 1 not in num_set:
            tmp = 0
            while tmp + n in num_set:
                tmp += 1
            res = max(res, tmp)

    return res