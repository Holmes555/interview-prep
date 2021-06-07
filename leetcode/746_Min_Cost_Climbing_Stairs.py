from math import inf
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        i = 0

        if l < 3:
            return min(cost)

        cost.extend([0, 0])
        res = [inf] * (l + 2)
        res[0], res[1] = cost[0], cost[1]

        while i < l - 1:
            a = res[i] + cost[i + 2]
            b = res[i + 1] + cost[i + 2]
            c = res[i + 1] + cost[i + 3]
            res[i + 2] = min(res[i + 2], a, b)
            res[i + 3] = min(res[i + 3], c)
            i += 1

        return res[-2]
