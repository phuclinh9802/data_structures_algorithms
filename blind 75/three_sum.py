class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            store = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = store + nums[j] + nums[k]

                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum == 0:
                    result.append([store, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:  # skip duplicates
                        j += 1

        return result
