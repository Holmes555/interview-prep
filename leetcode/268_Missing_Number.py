from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = sum(nums)
        b = sum(range(len(nums) + 1))
        return b - a
