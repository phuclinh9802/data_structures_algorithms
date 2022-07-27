class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        track1, track2 = 0, len(height) - 1
        store_max = 0

        while track1 <= track2:
            area = min(height[track1], height[track2]) * (track2 - track1)
            store_max = max(store_max, area)

            if height[track1] <= height[track2]:
                track1 += 1
            else:
                track2 -= 1

        return store_max
