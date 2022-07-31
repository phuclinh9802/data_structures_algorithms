class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        current = nums[start]

        if nums[start] <= nums[end]:
            return nums[start]

        while start <= end:
            mid = start + (end - start) // 2
            if start == end:
                current = min(current, nums[mid])
                break
            current = min(current, nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid - 1

        return current



