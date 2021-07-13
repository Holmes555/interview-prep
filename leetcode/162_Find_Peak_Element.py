from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i, v in enumerate(nums):
            if 0 < i < len(nums) - 1:
                if nums[i - 1] < v > nums[i + 1]:
                    return i
            elif i == 0:
                if v > nums[i + 1]:
                    return i
            else:
                if v > nums[i - 1]:
                    return i
