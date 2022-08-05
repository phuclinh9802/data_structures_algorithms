def longest_increasing_subsequence(nums):
    # dp bottom-up approach
    # base case, every element has at least 1 increasing subsequence, so we initialize dp list with els = 1
    dp = [1] * len(nums)

    # nested loop,
    # outer loop will be from last el to first el
    # inner loop will be from current outer loop element -> last elemen, e.g.: i = 2, j = 3,4; i = 1; j = 2,3,4
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)
