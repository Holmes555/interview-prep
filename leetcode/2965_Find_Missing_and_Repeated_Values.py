from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = set()
        missing = -1
        doubled = -1
        for row in grid:
            for num in row:
                if num in nums:
                    doubled = num
                else:
                    nums.add(num)
        l = len(grid) ** 2
        for i in range(1, l + 1):
            if i not in nums:
                missing = i
                break
        return [doubled, missing]
