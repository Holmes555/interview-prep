from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        q = [(temperatures[0], 0)]
        res = [0] * l

        for i in range(1, l):
            temp = temperatures[i]
            for j in range(len(q) - 1, -1, -1):
                if temp > q[j][0]:
                    res[q[j][1]] = i - q[j][1]
                    q.pop()
                else:
                    break
            q.append((temp, i))

        return res
