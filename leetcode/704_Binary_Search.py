from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
