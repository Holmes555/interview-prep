from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        prev = float('-inf')
        res = 0

        for n in nums:
            cur = min(max(prev + 1, n - k), n + k)
            if prev != cur:
                res += 1
                prev = cur
        return res
