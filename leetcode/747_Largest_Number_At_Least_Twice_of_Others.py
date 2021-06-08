from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        cm = lm = 0
        mi = 0

        for i, v in enumerate(nums):
            if v > cm:
                lm = cm
                cm = v
                mi = i
            if v > lm and v != cm:
                lm = v

        return mi if cm >= 2 * lm else -1
