from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False

        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        position = {grid[i][j]: (i, j) for i in range(n) for j in range(n)}

        for i in range(n * n - 1):
            x1, y1 = position[i]
            x2, y2 = position[i + 1]
            if (x2 - x1, y2 - y1) not in moves:
                return False

        return True
