from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = len(nums)
        max_count = 0
        zeros = 0
        i = 0
        while i < l:
            if nums[i] < 0:
                max_count += 1
            elif nums[i] == 0:
                zeros += 1
            else:
                break
            i += 1
        return max(max_count, l - zeros - max_count)
