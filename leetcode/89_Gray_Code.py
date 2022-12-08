from math import log
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]
        seq = [1]
        j = 1

        for i in range(2**n - 2):
            v = res[-1]
            l = log((i + 2), 2)
            if l.is_integer():
                l = int(l)
                j = len(seq)
                adding = 2**l
                next_v = v + adding
                seq.append(adding)
            else:
                j -= 1
                adding = -seq[j]
                next_v = v + adding
                seq.append(adding)
            res.append(next_v)
        return res
