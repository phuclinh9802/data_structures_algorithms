class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        for i, n in enumerate(nums):
            # [3, 0, 1]
            # res = (1, 2, 3) - (3, 0, 1)
            res += ((i + 1) - nums[i])

        return res