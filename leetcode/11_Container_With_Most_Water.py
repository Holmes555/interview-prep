from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        for i in range(1, len(height)):
            for j in range(i):
                area = (i - j) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
        return max_area


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
