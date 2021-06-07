from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        for i in range(1, l):
            if sum(nums[: i - 1]) == sum(nums[i:]):
                return i - 1
        if sum(nums[:i]) == 0:
            return i
        return -1
