def decode_ways(s):
    # this problem, we use dfs approach with caching dp to cache the result of the current char at i
    # to check how many ways from i
    # init the dp object with key being len(s) and value = 1 if we have empty s
    dp = {len(s) : 1}

    def dfs(i):
        # base case
        # when we found the value cached in dp object, or i reached len(s)
        if i in dp:
            return dp[i]
        # when the init character is 0 -> we can't continue with 0 as the start
        if s[i] == "0":
            return 0

        # else, do dfs like fibonacci, and we draw out the decision tree
        res = dfs(i + 1)

        # check if i + 1 is in bound and
        # check for next character after i if i = 1 or i = 2 and i + 1 = 0 -> 6 -> dfs(i + 2) also
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
            res += dfs(i + 2)

        # cache the current res for later
        dp[i] = res

        return res

    return dfs(0)


    # another way: iterative dp approach
    dp = {len(s) : 1}

    for i in range(len(s) - 1, -1, -1):
        # base case
        # current char is 0
        if s[i] == "0":
            dp[i] = 0

        else:
            dp[i] = dp[i + 1]

        # for the next digit if char at i is 1 or 2
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
            dp[i] += dp[i + 2]

    return dp[0]


