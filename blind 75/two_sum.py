def two_sum(nums, target):
    # brute force

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


def two_sum_hash(nums, target):
    # hash map
    hash_map = {}

    for i, n in enumerate(nums):
        hash_map[n] = i

    for i,n in enumerate(nums):
        diff = target - n
        if diff in hash_map and hash_map[diff] != i:
            return [i, hash_map[diff]]

