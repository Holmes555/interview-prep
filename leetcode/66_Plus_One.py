from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while True:
            if i < 0:
                digits.insert(0, 0)
                i = 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
            i -= 1
        return digits
