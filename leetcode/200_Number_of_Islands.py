from queue import Queue
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = Queue()
        s = set()
        res = 0

        def add_to_q(i, j):
            if grid[i][j] == '1' and (i, j) not in s:
                q.put((i, j))
                s.add((i, j))
                return True
            return False

        def check_neighbours(i, j):
            if j != 0:
                add_to_q(i, j - 1)
            if i != 0:
                add_to_q(i - 1, j)
            if j != m - 1:
                add_to_q(i, j + 1)
            if i != n - 1:
                add_to_q(i + 1, j)

        for i in range(n):
            for j in range(m):
                if add_to_q(i, j):
                    while not q.empty():
                        el = q.get()
                        check_neighbours(*el)
                    res += 1

        return res
