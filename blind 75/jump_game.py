class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy algorithm bottom-up
        # we check if the current index + number of steps can achieve the
        # current goal post, if the sum < goal post -> can't achieve yet and
        # need to traverse to check again.
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, - 1):
            sum = i + nums[i]
            if sum >= goal:
                goal = i
            if goal == 0:
                return True

        return False
