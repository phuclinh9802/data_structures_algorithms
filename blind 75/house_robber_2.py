class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        p_1 = p_2 = p_3 = p_4 = 0

        for i in range(len(nums) - 1):
            temp = max(nums[i] + p_1, p_2)
            p_1 = p_2
            p_2 = temp

        for i in range(len(nums) - 1, 0, -1):
            temp = max(nums[i] + p_4, p_3)
            p_4 = p_3
            p_3 = temp

        return max(p_2, p_3)