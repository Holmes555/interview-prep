from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, first in enumerate(numbers):
            second = target - first
            try:
                j = numbers[i + 1 :].index(second) + i + 1
            except ValueError:
                continue
            if i == j:
                continue
            return [i + 1, j + 1]
