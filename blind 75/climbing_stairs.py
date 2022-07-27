class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # climbing stairs is the same as fibonacci

        #         # memoization approach
        #         # create dictionary
        #         # create store to store value of current stair
        #         dictionary = {}
        #         f = 0
        #         # base case:
        #         if n in dictionary:
        #             return dictionary[n]

        #         if n == 0 or n == 1:
        #             f = 1

        #         # else
        #         elif n > 1:
        #             f = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        #             dictionary[n] = f

        #         return f

        # dp approach: 2 pointers
        p1 = p2 = 1
        for i in range(n - 1):
            temp = p1
            p1 += p2
            p2 = temp

        return p1
