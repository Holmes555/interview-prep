from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        changes = True

        iteration = True
        index = [0, -1]

        if n == 1:
            while iteration:
                try:
                    index[0] = mat[0].index(0, index[1] + 1)
                    index[0], index[1] = index[1], index[0]
                except ValueError:
                    iteration = False
                    index[0], index[1] = index[1], m
                for i in range(index[0] + 1, index[1]):
                    if mat[0][i] != 0:
                        if not iteration:
                            dist = abs(index[0] - i)
                        elif index[0] == -1:
                            dist = abs(index[1] - i)
                        else:
                            dist = min(abs(index[0] - i), abs(index[1] - i))
                        mat[0][i] = dist

        iteration = True
        index = [0, -1]

        if m == 1:
            while iteration:
                try:
                    index[0] = mat.index([0], index[1] + 1)
                    index[0], index[1] = index[1], index[0]
                except ValueError:
                    iteration = False
                    index[0], index[1] = index[1], m
                for i in range(index[0] + 1, index[1]):
                    if mat[i][0] != 0:
                        if not iteration:
                            dist = abs(index[0] - i)
                        elif index[0] == -1:
                            dist = abs(index[1] - i)
                        else:
                            dist = min(abs(index[0] - i), abs(index[1] - i))
                        mat[i][0] = dist

        def min_neighbours(i, j):
            a = []
            if j != 0:
                a.append(mat[i][j - 1])
            if i != 0:
                a.append(mat[i - 1][j])
            if j != m - 1:
                a.append(mat[i][j + 1])
            if i != n - 1:
                a.append(mat[i + 1][j])
            return min(a)

        while changes:
            changes = False
            for i in range(n):
                for j in range(m):
                    if mat[i][j] != 0:
                        new_v = min_neighbours(i, j) + 1
                        if mat[i][j] != new_v:
                            mat[i][j] = new_v
                            changes = True

        return mat
