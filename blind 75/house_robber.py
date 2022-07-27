class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p_1 = p_2 = 0

        for i in range(len(nums)):
            temp = max(nums[i] + p_1, p_2)
            p_1 = p_2
            p_2 = temp

        return p_2