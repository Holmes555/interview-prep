import math
from typing import List


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        temp_l = nums[: l - k]
        temp_r = nums[l - k :]
        nums[:k] = temp_r
        nums[k:] = temp_l


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        if k == 0:
            return
        j = k
        w = math.gcd(l, k)
        m = l / w
        temp = nums[0]
        for i in range(l):
            nums[j], temp = temp, nums[j]
            if (i + 1) % m == 0:
                j += 1
                temp = nums[j]
            j = (j + k) % l
