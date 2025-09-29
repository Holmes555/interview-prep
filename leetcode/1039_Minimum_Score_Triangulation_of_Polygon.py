from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        min_score = float('inf')

        for i in range(len(values)):
            queue = values.copy()
            for j in range(i):
                queue.append(queue[j])
            triangles = []
            while True:
                if i + 2 >= len(queue):
                    break
                a, b, c = queue[i], queue[i + 1], queue[i + 2]
                triangles.append(a * b * c)
                queue.append(queue[i])
                i += 2
            sum_triangles = sum(triangles)
            if min_score > sum_triangles:
                min_score = sum_triangles

        return min_score


class Solution2:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])

        return dp[0][n - 1]
