from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2:
            return l
        try:
            n = nums.index(0)
        except:
            return l

        i = n
        k = 1
        for j in range(n + 1, l):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            else:
                k += 1
        nums[l - k :] = [0] * k
