from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_array = []
        middle_array = []
        right_array = []
        for num in nums:
            if num < pivot:
                left_array.append(num)
            elif num == pivot:
                middle_array.append(num)
            else:
                right_array.append(num)
        return left_array + middle_array + right_array
