from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, first in enumerate(nums):
            second = target - first
            try:
                j = nums.index(second)
            except ValueError:
                continue
            if i == j:
                continue
            return [i, j]
