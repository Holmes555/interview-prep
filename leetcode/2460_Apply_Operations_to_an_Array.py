from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [[], []]
        i = 0
        while i < l:
            if nums[i] == 0:
                result[1].append(0)
            elif i + 1 < l and nums[i] == nums[i + 1]:
                result[0].append(nums[i] * 2)
                result[1].append(0)
                i += 1
            else:
                result[0].append(nums[i])
            i += 1
        return result[0] + result[1]
