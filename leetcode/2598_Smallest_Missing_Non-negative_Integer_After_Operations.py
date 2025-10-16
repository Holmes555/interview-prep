from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        seq = {i for i in range(n)}

        for num in nums:
            old_num = num
            while num >= 0:
                if num in seq:
                    seq.remove(num)
                num -= value

            while old_num <= n:
                if old_num in seq:
                    seq.remove(old_num)
                old_num += value

        return min(seq) if seq else n


class Solution2:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem = [0] * value
        for x in nums:
            rem[x % value] += 1
        res = 0
        while rem[res % value]:
            rem[res % value] -= 1
            res += 1
        return res
