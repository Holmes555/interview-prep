from typing import List


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        horizontalCuts.sort()
        verticalCuts.sort()

        h_max = 0
        v_max = 0

        for i in range(len(horizontalCuts) - 1):
            dist = horizontalCuts[i + 1] - horizontalCuts[i]
            if dist > h_max:
                h_max = dist

        for i in range(len(verticalCuts) - 1):
            dist = verticalCuts[i + 1] - verticalCuts[i]
            if dist > v_max:
                v_max = dist

        return h_max * v_max % (10 ** 9 + 7)
