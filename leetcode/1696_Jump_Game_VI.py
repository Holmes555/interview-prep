from math import inf
from typing import List
from functools import lru_cache


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        @lru_cache
        def memo_jump(n, m):
            return memo[n - m] + nums[n]

        res = nums[0]
        i = 0
        l = len(nums) - 1

        while True:
            if i >= l:
                return res
            ind = min(l, i + k)
            if nums[ind] >= 0:
                res += sum(filter(lambda x: x > 0, nums[i + 1 : ind + 1]))
                i = ind
            else:
                next_max = max(nums[i + 1 : ind + 1])
                j = ind - nums[ind:i:-1].index(next_max) - i - 1
                if next_max >= 0:
                    res += sum(filter(lambda x: x > 0, nums[i + 1 : i + j + 2]))
                    i += j + 1
                elif ind < l - 1:
                    ind2 = min(l, ind + k)
                    n_next_max = max(nums[ind + 1 : ind2 + 1])
                    h = nums[i + k + 1 : ind + k + 1].index(n_next_max) + ind
                    if h - j < k:
                        res += next_max
                        i += j + 1
                    else:
                        break
                else:
                    break

        memo = nums[:]
        memo[i] = res
        for n in range(i + 1, l + 1):
            max_t = -inf
            for m in range(1, k + 1):
                if m > n - i:
                    break

                t = memo_jump(n, m)
                if t > max_t:
                    max_t = t
            memo[n] = max_t

        return memo[-1]
