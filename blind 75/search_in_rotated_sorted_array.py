class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) / 2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[start]:
                if nums[mid] < target or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] <= nums[end]:
                if nums[mid] > target or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1

