from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        modulefinder = 10 ** 9 + 7
        result = 0
        number_of_odd = 0
        number_of_even = 0
        count = 0
        for num in arr:
            result += num
            if result % 2 == 0:
                count += number_of_odd
                number_of_even += 1
            else:
                count += number_of_even + 1
                number_of_odd += 1
        return count % modulefinder
