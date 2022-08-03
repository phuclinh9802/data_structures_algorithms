class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for n in nums:
            if n in hash_map:
                return True

            hash_map[n] = 1

        return False