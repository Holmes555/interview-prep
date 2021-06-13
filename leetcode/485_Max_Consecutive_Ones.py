from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        c = 0
        for i in nums:
            if i == 1:
                c += 1
            else:
                c = 0
            if c > m:
                m = c
        return m
