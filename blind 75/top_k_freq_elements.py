def top_k_freq_element(nums, k):
    # base case
    if k > len(nums):
        return []

    hash_map = {}

    for n in nums:
        if n in hash_map:
            hash_map[n] += 1
        else:
            hash_map[n] = 1

    res = []
    i = 0

    while i < k:
        store = 0 # this is to store the key with max value
        max = -float("Inf") # update max value
        for k, v in hash_map.items():
            if v > max:
                max = v
                store = k
        res.append(store)
        # set current value of store key to 0 to continue
        hash_map[store] = 0
        i += 1

    return res

    