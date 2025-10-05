from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]

        def dfs(r: int, c: int, reachable: List[List[bool]]):
            if reachable[r][c]:
                return
            reachable[r][c] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)

        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols - 1, atlantic_reachable)

        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows - 1, c, atlantic_reachable)

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result
