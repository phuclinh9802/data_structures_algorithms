def character_replacement(s, k):
    # for this problem, we use 2 pointers left and right, sliding window problem
    # with hash map to keep track of the longest freq. character
    count = {}
    res = 0

    l = 0

    # loop through s
    for r in range(len(s)):
        # update current character's frequency
        count[s[r]] = 1 + count.get(s[r], 0)

        # while the length of window (r - l + 1) - max(count.values()) > # of constrained operations to replace
        while (r - l + 1) - max(count.values()) > k:
            # decrement left pointer's character's count by 1
            count[s[l]] -= 1
            # move right the left pointer
            l += 1

        # then, we update the result with the window length
        res = max(res, r - l + 1)

    return res


