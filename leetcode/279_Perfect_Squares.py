from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        root = int(sqrt(n))
        sqrt_l = [i ** 2 for i in range(100, 0, -1) if i <= root]
        result = 10 ** 4

        def dfs(target, path, start):
            nonlocal result
            if len(path) > result:
                return 1
            if target == 0:
                result = len(path)
                return 2
            for i in range(start, len(sqrt_l)):
                val = sqrt_l[i]
                new_target = target - val
                if new_target < 0:
                    continue
                steps = dfs(new_target, path + [val], i)
                if steps > 0:
                    return steps - 1
            return 0

        dfs(n, [], 0)
        return result
