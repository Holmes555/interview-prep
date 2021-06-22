from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex + 1):
            cur = [1] * (i + 1)
            for j in range(1, i):
                cur[j] = res[j - 1] + res[j]
            res = cur[:]

        return res
