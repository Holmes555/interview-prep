from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            i = 0
            robberies = 0
            while i < len(nums):
                if nums[i] <= mid:
                    i += 2
                    robberies += 1
                else:
                    i += 1

            if robberies >= k:
                right = mid
            else:
                left = mid + 1

        return left
