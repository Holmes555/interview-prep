from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(range(1, len(nums) + 1))
        for i in nums:
            if i in s:
                s.remove(i)
        return list(s)
