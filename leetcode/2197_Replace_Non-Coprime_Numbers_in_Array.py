import math
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        final_result = 1
        while True:
            result = []
            i = 0
            while i < len(nums):
                a = nums[i]
                j = i + 1
                while j < len(nums):
                    b = nums[j]
                    gcd = math.gcd(a, b)
                    if gcd > 1:
                        lcm = a * b // gcd
                        a = lcm
                        j += 1
                    else:
                        i = j - 1
                        break
                result.append(a)
                if j == len(nums):
                    break
                i += 1
            if len(result) == len(nums):
                break
            final_result *= -1
            nums = result[::-1]
        return result[::final_result]
