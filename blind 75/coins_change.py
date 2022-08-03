def coin_change(coins, amount):
    # dp approach
    dp = [amount + 1] * (amount + 1)
    # base case
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c])

    return dp[amount] if dp[amount] != amount + 1 else -1



# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # dp approach
#         dp = [amount + 1] * (amount + 1)
#         dp[0] = 0  # base case
#
#         for i in range(1, amount + 1):  # go through every amount available
#             for c in coins:  # go through each coin
#                 if i - c >= 0:  # if current amount can be combined by current c
#                     dp[i] = min(dp[i], 1 + dp[i - c])  # save current amount to
#                     # the min of itself (if calculated                                                           before) and recurrence relation
#                     # where we found one more way which satisfies the if statement (where 1 exists), and the saved amount i - c
#
#         return dp[amount] if dp[amount] != amount + 1 else -1
#

