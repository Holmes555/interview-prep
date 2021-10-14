from functools import reduce
from typing import List

# import numpy as np


class Solution:
    def mult(self, a, nums, l, r):
        if l > r:
            return 1
        if l == r:
            return nums[l]
        if a[l][r] is not None:
            return a[l][r]
        if r - l == 1:
            t = nums[l] * nums[r]
            a[l][r] = t
            return t
        # m = int((l + r) / 2)
        t = self.mult(a, nums, l, l) * self.mult(a, nums, l + 1, r)
        a[l][r] = t
        return t

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ind = set()
        l = len(nums)
        while True:
            try:
                i = nums.index(0)
                ind.add(i)
                nums[i] = 1
            except:
                break
        m = reduce(lambda x, y: x * y, nums)
        if len(ind) > 1:
            return [0 for _ in range(l)]
        if ind:
            return [m if i in ind else 0 for i in range(l)]
        return [int(m / i) for i in nums]

        # len_n = len(nums)
        # a = [[None for x in range(len_n)] for y in range(len_n)]
        # res = []
        # for i in range(len_n):
        #     res.append(self.mult(a, nums, 0, i-1) * self.mult(a, nums, i+1, len_n-1))
        # return res
