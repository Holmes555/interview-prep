from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = len(arr)
        counter = {}
        for el in arr:
            if el in counter:
                counter[el] += 1
            else:
                counter[el] = 1
        counter = sorted(counter.values(), reverse=True)
        res = 0
        count = 0
        while res < l / 2:
            count += 1
            res += counter.pop(0)
        return count
