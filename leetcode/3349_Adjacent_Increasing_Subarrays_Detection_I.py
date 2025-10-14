from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cur, prev, res = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                prev, cur = cur, 1
            res = max(res, min(prev, cur))
            res = max(res, cur // 2)
        return res >= k
