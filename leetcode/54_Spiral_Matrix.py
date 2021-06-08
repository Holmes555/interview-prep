from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        s = n * m

        n_t = [0, n]
        m_t = [0, m]
        way = 1

        i = j = 0

        res = []

        while s > 0:
            l = int((way - 1) / -2)
            k = int((way + 1) / 2)
            for j in range(m_t[l] - l, m_t[k] - l, way):
                res.append(matrix[i][j])
                s -= 1
            n_t[l] = i + k
            for i in range(n_t[l] - l, n_t[k] - l, way):
                res.append(matrix[i][j])
                s -= 1
            m_t[k] = j + l
            way *= -1

        return res
