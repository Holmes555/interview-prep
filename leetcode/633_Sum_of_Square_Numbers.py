from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = sqrt(c)
        if s.is_integer():
            return True
        s = int(s)

        for i in range(1, s + 1):
            other = c - i ** 2
            if sqrt(other).is_integer():
                return True

        return False
