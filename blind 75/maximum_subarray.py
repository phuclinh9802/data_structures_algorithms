class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force
        if len(nums) == 1:
            return nums[0]

        result = -float("Inf")
        current = 0

        for i in range(len(nums)):
            if current < 0:
                current = 0

            current += nums[i]
            result = max(result, current)

        return result