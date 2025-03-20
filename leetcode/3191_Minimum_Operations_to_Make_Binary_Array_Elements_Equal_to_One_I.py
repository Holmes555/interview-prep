from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == 1:
                i += 1
                continue
            if i + 2 < l:
                res += 1
                nums[i] = 1
                nums[i + 1] = int(nums[i + 1] == 0)
                nums[i + 2] = int(nums[i + 2] == 0)
                i += 1
            else:
                res = -1
                break
        return res
