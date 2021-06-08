import itertools
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat) - 1
        m = len(mat[0]) - 1

        if n == 0:
            return mat[0]
        if m == 0:
            return list(itertools.chain(*mat))

        way = 1
        phase = [1, 1]
        i = j = 0
        res = []

        while i < n or j < m:
            res.append(mat[i][j])
            if way == 1:
                if phase[0] == 1:
                    if i == 0:
                        if j == m:
                            i += 1
                            phase[0] = 2
                        else:
                            j += 1
                        if j == m:
                            phase[0] = 2
                        way = -1
                        continue
                if phase[0] == 2:
                    if j == m:
                        i += 1
                        way = -1
                        continue
                i -= 1
                j += 1
            if way == -1:
                if phase[1] == 1:
                    if j == 0:
                        if i == n:
                            j += 1
                            phase[1] = 2
                        else:
                            i += 1
                        if i == n:
                            phase[1] = 2
                        way = 1
                        continue
                if phase[1] == 2:
                    if i == n:
                        j += 1
                        way = 1
                        continue
                i += 1
                j -= 1
        res.append(mat[i][j])
        return res
