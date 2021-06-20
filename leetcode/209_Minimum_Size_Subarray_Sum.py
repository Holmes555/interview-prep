from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        min_l = l
        sums = sum(nums)
        if sums < target:
            return 0
        if sums == target:
            return min_l
        m = max(nums)
        if m >= target:
            return 1
        i = j = 0
        cur_sum = nums[0]
        while j <= i:
            for i in range(i + 1, l):
                cur_sum += nums[i]
                if cur_sum >= target:
                    min_l = min(min_l, i - j + 1)
                    break
            while True:
                cur_sum -= nums[j]
                j += 1
                if cur_sum >= target:
                    min_l = min(min_l, i - j + 1)
                else:
                    break
            if min_l == 2:
                break
        return min_l
