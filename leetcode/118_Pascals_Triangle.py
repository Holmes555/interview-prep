from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]

        for i in range(2, numRows):
            cur = [1] * (i + 1)
            for j in range(1, i):
                cur[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(cur)

        return res
