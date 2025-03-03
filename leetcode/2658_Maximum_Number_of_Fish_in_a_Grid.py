from typing import List


class Solution:

    def __init__(self):
        self.v = set()
        self.n = 0
        self.m = 0

    def traverse(self, i, j):
        a = set()
        if j != 0:
            a.add((i, j - 1))
        if i != 0:
            a.add((i - 1, j))
        if j != self.m - 1:
            a.add((i, j + 1))
        if i != self.n - 1:
            a.add((i + 1, j))
        return a

    def rec(self, coords, board):
        if coords in self.v:
            return 0
        result = 0

        i, j = coords
        if board[i][j] == 0:
            return result
        else:
            result += board[i][j]
            self.v.add(coords)
            a = self.traverse(i, j)
            for c in a:
                result += self.rec(c, board)
        return result

    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fish = 0

        self.n = len(grid)
        self.m = len(grid[0])

        for i in range(self.n):
            for j in range(self.m):
                temp_max_fish = self.rec((i, j), grid)
                if temp_max_fish > max_fish:
                    max_fish = temp_max_fish

        return max_fish
